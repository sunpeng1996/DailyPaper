---
title: '4DAnyone: Create Anyone in 4D from a Casual Monocular Video'
title_zh: 4DAnyone：基于任意单目视频的4D人体重建框架
authors:
- Yudong Jin
- Tao Xie
- Qihang Zhang
- Zehong Shen
- Zhen Xu
- Yujun Shen
- Hujun Bao
- Xiaowei Zhou
- Yinghao Xu
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
- Robbyant
- Chinese University of Hong Kong
- Ant Group
- Hong Kong University of Science and Technology
arxiv_id: '2608.20335'
url: https://arxiv.org/abs/2608.20335
pdf_url: https://arxiv.org/pdf/2608.20335
published: '2026-08-19'
collected: '2026-08-21'
category: Other
direction: 4D生成 · 多视图一致性优化
tags:
- 4D Reconstruction
- Gaussian Splatting
- Video Diffusion
- Multiview Consistency
- DiT
one_liner: 通过RCP和TCR设计解决多视图一致性瓶颈，实现任意单目视频的4D人体重建
practical_value: '- 可借鉴RCP固定长度上下文压缩思路，优化多模态召回/长序列用户建模的特征存储与推理效率

  - 可复用TCR分块上下文路由逻辑，解决大批次LLM推理时跨特征/跨样本的一致性漂移问题

  - 多视图一致性优化方案可迁移到电商商品3D/4D建模场景，降低商品高精度建模的硬件门槛'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有相机可控视频扩散模型生成多视图视频时，若目标视图数量超出单步DiT推理容量会出现两大瓶颈：参考上下文复杂度随视图数线性增长弱化跨视图外观引导，分块视图缺乏信息交互导致全局结构漂移，无法满足4D Gaussian Splatting (4DGS) 重建所需的数十视角一致性要求。
### 方法关键点
1. 提出Reference Context Packing (RCP)，将增长的参考视图压缩为固定长度混合分辨率上下文，实现O(1)复杂度的参考上下文建模
2. 提出Target Context Routing (TCR)，在去噪阶段旋转目标视图分组，高噪声步跨组共享上下文、低噪声步稳定细节
3. 构建MVGameHuman数据集，结合光场、野外视频数据集联合训练
### 关键结果
在DNA-Rendering和DyMVHumans数据集上，新视角视频质量、下游4DGS重建效果均优于SOTA，具备强野外泛化能力
