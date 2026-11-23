---
title: 'cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction'
title_zh: cmHC：通过几何收缩平衡超连接中的流混合
authors:
- Haowei He
- Ziwen Zhao
- Chenshuo Pan
- Gang Lin
- Zhihao Yang
- Chao Wang
- Xinzhang Liu
- Kaidong Yu
- Han Gao
- Dongfang Li
affiliations:
- Xingchen AGI Lab, China Telecom
- The Hong Kong University of Science and Technology (Guangzhou)
- Harbin Institute of Technology (Shenzhen)
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.27193'
url: https://arxiv.org/abs/2611.27193
pdf_url: https://arxiv.org/pdf/2611.27193
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 大模型训练 · 超连接流混合优化
tags:
- Hyper-Connections
- Birkhoff-Polytope
- LLM-Pretraining
- Mixture-of-Experts
- Fused-Operator
one_liner: 针对超连接流混合的欠/过混合权衡问题，提出无额外参数的cmHC方法，兼容大模型训练且延迟最高降44.8%
practical_value: '- 若业务中使用mHC/mHC-lite搭建生成式推荐/Agent垂直大模型，可直接替换为cmHC，无需新增参数，仅对前2-5层设置λ=0.96~0.97的适度收缩，即可降低训练损失并提升梯度稳定性

  - 推荐多兴趣建模、多模态特征融合等多流交互场景，可借鉴Birkhoff polytope几何收缩思路，无额外参数即可平衡特征交互强度，避免欠融合或过拟合

  - 硬件部署阶段可参考其融合算子设计，将系数生成、特征聚合、残差混合等小算子合并，在Ascend NPU上可降低超连接模块延迟最高44.8%'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于双随机约束的超连接（mHC、mHC-lite）存在流混合权衡痛点：欠混合时残差矩阵长期贴近Birkhoff polytope的置换顶点，多流退化为近乎独立的通路，浪费多流架构的表达能力；过混合时残差矩阵向polytope均匀重心收敛，流间区分度消失，反而损害模型效果。此前优化方法要么引入复杂参数化无明确混合效果保障，要么未在超大规模MoE模型上验证可行性。
### 方法关键点
- 提出几何收缩操作，将Birkhoff polytope的顶点置换矩阵替换为平滑版本，无额外新增参数，严格保留双随机性质，且有可证明的流混合下界，从根本上避免欠混合问题
- 揭示收缩的“蝴蝶效应”：浅层收缩的混合效果会随层数累积放大，易导致深层过混合，因此仅对前2-5个浅层施加λ=0.96~0.97的适度收缩，深层保留原置换矩阵，平衡混合收益与流区分度
- 针对Ascend NPU定制融合算子，合并系数生成、流聚合、残差混合等多个小算子，大幅降低执行开销
### 关键实验
在OpenWebText、FineWeb-Edu数据集上对比Residual、HC、mHC、mHC-lite等基线：nanoGPT全系列验证集损失比mHC-lite最高降低0.0073；6B/300B参数MoE模型上训练损失比mHC低0.002~0.0157，梯度波动更小；定制融合算子在Ascend 910C上最高降低超连接模块执行延迟44.8%。
> 最值得记住的结论：多流特征交互无需盲目追求全层高强度混合，仅在浅层施加无参数的适度约束，就能同时获得性能收益与训练稳定性。
