import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
function TableComponent(props) {
  console.log(props, "k xa table ma")
  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Title</th>
          <th>StoryLine</th>
          <th>Is Active</th>
          <th>Ceated At</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {
            props.movies && props.movies.map((item,index)=>{
                return(
                    <tr key = {index}>
                    <td>{item.title}</td>
                        <td>{item.storyline}</td>
                        <td>{item.active ? "Active" : "Inactive"}</td> {/* */}
                        <td>{item.created_at}</td> 
                        <td>
                          <Button onClick = {() => props?.onEdit(item)}>
                          Edit
                          </Button>
                          <Button variant = "danger" onClick = {() => props?.onDelete(item.id)} >
                            Delete
                          </Button>
                        </td>
                    </tr>
                );
            })
        }
      </tbody>
    </Table>
  );
}

export default TableComponent;