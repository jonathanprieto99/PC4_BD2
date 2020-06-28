$(function(){
    $("#gallery").dxGallery({
        dataSource: "galeria",
        height: 440,
        width: "100%",
        loop: true,
        showIndicator: false,
        itemTemplate: function (item, index) {
            var result = $("<div>");
            $("<img>").attr("src", item.Image).appendTo(result);
            $("<div>").addClass("item-price").text(item.Score, { maximumFractionDigits: 0 }).appendTo(result);
            return result;
        }
    });
});