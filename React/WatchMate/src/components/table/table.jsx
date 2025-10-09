import Table from 'react-bootstrap/Table';

function TableComponent(props) {
  // console.log(props, "k xa table ma")
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Title</th>
          <th>StoryLine</th>
          <th>Is Active</th>
          <th>Ceated At</th>
        </tr>
      </thead>
      <tbody>
        {
            props.movies && props.movies.map((item,index)=>{
                return(
                    <tr key = {index}>
                    <td>{item.title}</td>
                        <td>{item.storyline}</td>
                        <td>{item.active ? "Active" : "Inactive"}</td>
                        <td>{item.created_at}</td> 
                    </tr>
                );
            })
        }
      </tbody>
    </Table>
  );
}

export default TableComponent;