---
title: 'PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model'
title_zh: PINE：单步扩散模型实现点云、实例与法向量联合估计
authors:
- Zeyu Ren
- Jie Ni
- Rui Qian
- Jiahao Wei
- Hao Tang
- Yongtai Liu
- Zeyu Zhang
affiliations:
- The University of Melbourne
- Southeast University
- Fudan University
- Peking University
- Hanyang University
arxiv_id: '2611.29389'
url: https://arxiv.org/abs/2611.29389
pdf_url: https://arxiv.org/pdf/2611.29389
published: '2026-11-21'
collected: '2026-11-25'
category: Other
direction: 单步扩散模型 · 多任务3D场景理解
tags:
- Diffusion Model
- Transformer
- 3D Scene Understanding
- Multi-task Learning
- DINOv3
one_liner: 提出单步扩散Transformer PINE，单次前向同时输出点云、表面法向量、实例分割三类结果
practical_value: '- 多任务token流加掩码控制交互的设计，可迁移至多任务LLM4Rec架构，对用户/物品/上下文不同token流做交互范围约束，降低计算开销同时提升任务效果

  - Grounding attention将预训练特征亲和度直接注入注意力logits的技巧，可复用在RAG生成环节，提升生成结果和检索上下文的语义对齐度

  - 小样本合成数据训练达到SOTA的策略，可借鉴到电商冷启动场景（新品类推荐、低活用户建模）的模型训练'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D场景理解需要通过不同网络或多次前向分别计算几何（点云、法向量）和语义（实例分割）结果，链路长、延迟高，缺乏单步多输出的统一方案。
### 方法关键点
1. 提出单步Omni Diffusion Transformer架构PINE，将三类输出映射各自作为独立token流，通过流掩码控制不同流的交互逻辑；
2. 采用相机感知射线编码替代传统像素位置编码，基于相机射线给token做空间定位；
3. 设计Grounding attention，将预训练DINOv3特征的亲和度注入注意力logits，提升语义对齐能力。
### 关键结果
仅用139K合成图像训练几何任务，点云预测无论是否给定相机内参均达SOTA，表面法向量平均排名最优；大物体实例分割效果超过SAM，训练数据量仅为后者1%以下；三类结果联合预测速度比MoGe-3+SAM组合快5.7倍。
