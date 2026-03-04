async function submitAbstract() {

    const abstract = document.getElementById("abstract").value;
    const style = document.getElementById("style").value;

    const response = await fetch("http://localhost:8000/improve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ abstract, style })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.improved;
}
