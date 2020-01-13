/* <div id="content"> */
let div0 = document.getElementById("main")
let div1 = document.createElement("div");
let id1 = document.createAttribute("id");
id1.value = "content";
div1.setAttributeNode(id1);
div0.appendChild(div1);

for (let i=1; i<=2; i++) {
    /* <div class="content-post"> */
    let div2 = document.createElement("div");
    let class0 = document.createAttribute("class");
    class0.value = "content-post";
    div2.setAttributeNode(class0);
    div1.appendChild(div2);

    if (i === 1) {
        /* <h1>Judul Post</h1> */
        let h10 = document.createElement("h1");
        let judulPost = document.createTextNode("Judul Post");
        h10.appendChild(judulPost);
        div2.appendChild(h10);
    }

    else {
        /* <h1>Judul Post</h1> */
        let h10 = document.createElement("h1");
        let judulPost = document.createTextNode("Judul Post "+(i).toString());
        h10.appendChild(judulPost);
        div2.appendChild(h10);
    }

    /* <span>Published on 12 May 2016</span> */
    let span0 = document.createElement("span");
    let published = document.createTextNode("Published on "+(11+i).toString()+" May 2016");
    span0.appendChild(published);
    div2.appendChild(span0);

    /* <p>Lorem Ipsum Dolor Sit Amet</p> */
    let p0 = document.createElement("p");
    let lorem = document.createTextNode("Lorem Ipsum Dolor Sit Amet");
    p0.appendChild(lorem);
    div2.appendChild(p0);

    /* <button class="share-post-btn">Share this Post</button> */
    let button0 = document.createElement("button");
    let class1 = document.createAttribute("class");
    class1.value = "share-post-btn";
    button0.setAttributeNode(class1);
    let share = document.createTextNode("Share this Post");
    button0.appendChild(share);
    div2.appendChild(button0);

    document.getElementsByClassName("share-post-btn")[i-1].addEventListener("click", functionShare);

    function functionShare() {
        alert ("You have shared this post!");
    }
}






