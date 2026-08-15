---
title: 'GeoCache: Training-Free Acceleration of Multi-View Texture Diffusion via Geometric
  Delta Transport'
title_zh: GeoCache：基于几何增量传输的免训练多视图纹理扩散加速
authors:
- Haotang Li
- Zhenyu Qi
- Shaohan Henry Wang
- Kebin Peng
- Yutong Zhao
- Zi Wang
- Bo Liu
- Huanrui Yang
- Sen He
affiliations:
- University of Arizona
- East Carolina University
- California State University, Long Beach
- Augusta University
arxiv_id: '2608.13255'
url: https://arxiv.org/abs/2608.13255
pdf_url: https://arxiv.org/pdf/2608.13255
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 多视图扩散模型 · 免训练推理加速
tags:
- Diffusion Model
- Training-free
- Multi-view Generation
- Inference Acceleration
- 3D Texture
one_liner: 提出免训练GeoCache插件，利用跨视图几何对应性传输更新，实现多视图纹理扩散2倍以上加速且保真度更优
practical_value: '- 免训练插件设计思路可直接复用在电商多视角商品图/3D商品生成场景的推理加速，无需修改原模型、无需重训，落地成本极低

  - 跨维度复用计算的思路可拓展到生成式推荐场景：除了常用的时序KV cache，可挖掘语义/特征对应维度（如同商品不同渲染视图、同用户不同场景召回结果）的冗余，进一步降低推理成本

  - 「部分采样+周期性全量校正控误差」的trick可复用在流式推荐、增量更新场景，平衡推理效率和效果精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
几何条件多视图扩散可生成高质量3D纹理，但逐视图重复降噪计算成本极高；现有免训练加速方案多复用时序冗余，跳过步骤会破坏跨视图一致性，导致保真度快速下降。
### 方法关键点
挖掘几何对应冗余：几何对齐的表面点的预测干净信号演化可跨视图迁移；推出GeoCache免训练插件，仅计算旋转子集的锚点视图降噪结果，将几何对齐的每步更新传输到其余视图；搭配周期性全视图计算控制累积误差，采样器一致性重建保留降噪轨迹，无需重训或改架构，复用现有管线的位置图即可。
### 关键结果
在Hunyuan3D-2.1、SyncMVD、MVPainter三类管线中，2×以上加速区间的速度-保真度trade-off优于时序缓存、步长缩减方案；在Hunyuan3D-2.1上实现2.21×降噪循环加速，MV-LPIPS 0.0293，MV-PSNR 33.60dB，是2×以上加速方案中保真度最高；在SyncMVD上获最高加速比和最低FLOPs，在MVPainter上获加速方案中最低FLOPs和最优保真度。
