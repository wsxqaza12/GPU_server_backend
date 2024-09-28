import grpc
import os
from gRPC import facefusion_pb2, facefusion_pb2_grpc
from config import Config

def sync_lip(source_paths, target_path, output_path):
    try:
        with grpc.insecure_channel(Config.SYNC_LIP_GRPC_SERVER_URL) as channel:
            stub = facefusion_pb2_grpc.FaceFusionStub(channel)
            response = stub.RunFaceFusion(facefusion_pb2.FaceFusionRequest(
                source_paths=[source_paths],
                target_path=target_path,
                output_path=output_path
            ))
        print("FaceFusion客户端收到: " + response.message)
        
        if response.success:
            return {'status': 'success', 'message': response.message}
        else:
            return {'status': 'error', 'message': response.message}
    except Exception as e:
        print(f"gRPC错误: {str(e)}")
        return {'status': 'error', 'message': f'视频处理失败: {str(e)}'}

if __name__ == '__main__':
    # 测试代码
    result = sync_lip(
        ["/home/user/facefusion/inputs/test.mp3"],
        "/home/user/facefusion/inputs/facefusion.mp4",
        "/home/user/facefusion/inputs/test_facefusion.mp4"
    )
    print(result)