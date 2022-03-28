import streamlit as st
import pandas as pd

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)




st.markdown("""
<!--Main Navigation-->
<header>
  <!-- Sidebar -->
  <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse">
    <div class="position-sticky ">
      <div class="list-group list-group-flush mx-3 mt-4 ">
        <a
          href="#"
          class="list-group-item list-group-item-action py-2 bg-dark ripple"
          aria-current="true">
          <i class="fas fa-tachometer-alt fa-fw me-3"></i><span>Main dashboard</span>
        </a>
        <a href="#" class="list-group-item list-group-item-action py-2 bg-dark ripple active">
          <i class="fas fa-chart-area fa-fw me-3"></i><span>Source Connectors</span>
        </a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-lock fa-fw me-3"></i><span>Transformations at Source</span></a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-chart-line fa-fw me-3"></i><span>Real Time Data Streaming</span></a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple">
          <i class="fas fa-chart-pie fa-fw me-3"></i><span>Transformation support</span>
        </a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-chart-bar fa-fw me-3"></i><span>Datawarehouse Destination</span></a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-globe fa-fw me-3"></i><span>Advantages/Limitation</span></a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"><i class="fas fa-building fa-fw me-3"></i><span>Cost</span></a>
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-calendar fa-fw me-3"></i><span>Support</span></a
        >
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-users fa-fw me-3"></i><span>Security</span></a
        >
        <a href="#" class="list-group-item list-group-item-action bg-dark py-2 ripple"
          ><i class="fas fa-money-bill fa-fw me-3"></i><span>Miscellaneous</span></a
        >
      </div>
    </div>
  </nav>
  <!-- Sidebar -->

""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" >
  <a class="navbar-brand " href="#" target="_blank">ETL/ELT Utility Tool</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-20">
      <li class="nav-item active ml-20" >
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" target="_blank">Your Choices</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/" target="_blank">Result</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# data = pd.read_csv("data//ETL-ELT Tool Accelerator_Finalized.xlsx - Detail Score.csv")

# first = data[["Platform Features"]]
# print(first)

# st.write(first)

data = pd.read_csv("data//Break-up of ETL-ELT Tool Accelerator.xlsx - Source Connectors.csv")

first = data["Platform Features"].dropna();
discard = ["description","Description"]
  
# drop rows that contain the partial string "description"
first = first[~first.str.contains('|'.join(discard))]
print(first)

st.write('Select feature:')
opts = list(first)
print(opts)

known_variables = {}
for i, todo_text in enumerate(opts):
        var = st.checkbox(label=f'{todo_text}', key=i)
        print(var)
        known_variables.update({todo_text:var})

print(known_variables)