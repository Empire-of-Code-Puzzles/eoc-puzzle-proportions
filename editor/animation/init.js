//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            var checkioInput = data.in;

            var strInput = JSON.stringify(checkioInput).replace(/\[(\d+),(\d+)\]/g, "Fraction($1, $2)");
            if (data.error) {
                $content.find('.call').html('Fail: checkio(' + strInput + ')');
                $content.find('.output').html(data.error.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
                return false;
            }

            var rightResult = data.ext["answer"];
            var userResult = data.out;
            var result = data.ext["result"];
            var result_addon = data.ext["result_addon"];


            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult).replace(/\[(\d+),(\d+)\]/g, "Fraction($1, $2)"));

            if (!result) {
                $content.find('.call').html('Fail: checkio(' + strInput + ')');
                $content.find('.answer').html('Right result:&nbsp;' + JSON.stringify(rightResult).replace(/\[(\d+),(\d+)\]/g, "Fraction($1, $2)"));
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: checkio(' + strInput + ')');
                $content.find('.answer').remove();
            }


            var canvas = new AlloysCanvas($content.find(".explanation")[0]);
            canvas.createCanvas(checkioInput, explanation);

            this_e.setAnimationHeight($content.height() + 60);

        });

       

        var colorOrange4 = "#F0801A";
        var colorOrange3 = "#FA8F00";
        var colorOrange2 = "#FAA600";
        var colorOrange1 = "#FABA00";

        var colorBlue4 = "#294270";
        var colorBlue3 = "#006CA9";
        var colorBlue2 = "#65A1CF";
        var colorBlue1 = "#8FC7ED";

        var colorGrey4 = "#737370";
        var colorGrey3 = "#9D9E9E";
        var colorGrey2 = "#C5C6C6";
        var colorGrey1 = "#EBEDED";

        var colorWhite = "#FFFFFF";


        function AlloysCanvas(dom) {
            var x0 = 10,
                x1 = 10,
                x2 = 100,
                y0 = 10;

            var r = 150;
            var cell = 30;
            var padding = 10;

            var fullSizeX = x0 * 2 + r * 2;
            var fullSizeY = y0 * 2 + r * 2 + cell * 3 + padding * 3;

            var paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0);

            var attrs = {
                'gold': {"stroke": colorGrey4, "stroke-width": 2, "fill": colorOrange4},
                'tin': {"stroke": colorGrey4, "stroke-width": 2, "fill": colorBlue1},
                'copper': {"stroke": colorGrey4, "stroke-width": 2, "fill": colorOrange1},
                'iron': {"stroke": colorGrey4, "stroke-width": 2, "fill": colorBlue3}
            };
            var attrText = {"stroke": colorBlue4, "font-size": cell * 0.6, "font-family": "Verdana"};

            var metals = ['gold', 'tin', 'copper', 'iron'];

            this.createCanvas = function(alloys, partitions) {
                var angle1 = 0,
                    angle2 = 0;
                var center = [fullSizeX / 2, y0 + r];
                for (var i = 0; i < 4; i++){
                    var p = partitions[metals[i]][0] / partitions[metals[i]][1];
                    angle2 = angle1 + Math.PI * 2 * p;
                    paper.path(Raphael.format(
                        "M{0},{1}L{2},{3}A{6},{6},{7},0,1,{4},{5}Z",
                        center[0],
                        center[1],
                        center[0] + Math.sin(angle1) * r,
                        center[1] - Math.cos(angle1) * r,
                        center[0] + Math.sin(angle2) * r,
                        center[1] - Math.cos(angle2) * r,
                        r,
                        angle2 - angle1
                    )).attr(attrs[metals[i]]);
                    angle1 = angle2;
                }
                var y1 = y0 + r * 2 + padding;
                var xText = x1 + cell * 2 + padding * 2 + x2;
                i = 0;
                for (al in alloys) {
                    var ms = al.split("-");
                    paper.rect(x1, y1 + (padding + cell) * i, cell, cell).attr(attrs[ms[0]]);
                    paper.rect(x1 + cell + padding, y1 + (padding + cell) * i, cell, cell).attr(attrs[ms[1]]);
                    paper.text(xText, y1 + (padding + cell) * i + cell / 2,
                        ms[0] + " + " + ms[1] + " = " + alloys[al][0] + "/" + alloys[al][1]
                        ).attr(attrText);
                    i++;
                }
            }

        }


    }
);
