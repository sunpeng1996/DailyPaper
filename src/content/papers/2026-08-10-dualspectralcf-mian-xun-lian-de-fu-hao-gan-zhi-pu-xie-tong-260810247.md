---
title: 'DualSpectralCF: Training-Free Sign-Aware Spectral Collaborative Filtering'
title_zh: DualSpectralCF：免训练的符号感知谱协同过滤
authors:
- Guanqun Yang
- Tong Qi
- Xiaoxue Han
affiliations:
- Stevens Institute of Technology
- University of Maryland, College Park
arxiv_id: '2608.10247'
url: https://arxiv.org/abs/2608.10247
pdf_url: https://arxiv.org/pdf/2608.10247
published: '2026-08-10'
collected: '2026-08-12'
category: RecSys
direction: 协同过滤 · 免训练负反馈建模
tags:
- Collaborative-Filtering
- Training-Free
- Negative-Feedback
- Spectral-Graph
- Recommendation
one_liner: 为现有免训练谱协同过滤扩展显式负反馈支持，兼顾精度提升与极高推理效率
practical_value: '- 负反馈建模可复用核心trick：不要将显式负反馈（差评、踩、低完播）直接赋值为负权重，最优γ恒为非正值，即给负反馈一个低于正交互的小正权重，同时覆盖品类兴趣信号与负向体验信号，可直接迁移到现有召回/排序模型的特征工程中

  - 现有线上免训练CF服务（如EASE、谱CF类召回）可快速改造：仅需修改用户交互向量编码、item-item相似度矩阵两个模块，新增2个超参数即可接入负反馈，无重新训练成本，适合快速迭代

  - 冷启动用户场景可优先落地：针对仅1-5个交互的新用户，该方法Recall@20最高提升29.2%，可单独为冷启动流量层配置该通路，快速提升新用户推荐体验

  - 高吞吐/低延迟场景选型参考：优先选择DualSpectralCF-Cheby版本，默认超参γ=-0.5、κ=0.1即可覆盖4/5场景，相比有训符号感知模型SIGformer快7.7~155.3倍，精度达后者70.7%~90.7%，性价比极高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有免训练谱CF方法性能接近甚至超过有训GNN推荐，计算成本极低，适合高吞吐推荐场景，但仅支持正交互建模，无法利用电商、内容平台普遍收集的1星差评、踩、低完播率等显式负反馈；而已有的符号感知推荐模型均依赖梯度训练，推理成本高、部署门槛高，二者之间存在能力空白。

### 方法关键点
- 框架兼容所有满足$Ër_u = F(M)r_u$形式的谱CF backbone，仅新增2个标量超参数$γ$、$κ$，全程无训练成本
- 符号化输入信号$r_u^\pm$：正交互赋值+1，显式负交互赋值$-\gamma$，实验验证最优$γ$恒为非正值，相当于给负反馈分配低于正交互的小正权重，同时覆盖用户品类兴趣与单物品负向体验
- 符号化item-item算子$M^\pm$：融合用户共同喜欢、共同讨厌的两类item相似度，$κ$控制负向相似度权重，保证原有低通滤波算子仍稳定有效

### 关键实验
在Amazon-CD/音乐、Epinions、快手KuaiRand/KuaiRec共5个带显式负反馈的数据集测试，对比ChebyCF、GF-CF、Turbo-CF等免训练基线，以及LightGCN、SIGformer等有训基线：所有DualSpectralCF实例均超过对应unsigned backbone，Recall@20最高提升32.6%；默认超参下Cheby版本提升1.9%~16%；比SIGformer快7.7~155.3倍，精度达后者70.7%~90.7%；冷启动用户（1~5个训练交互）最高提升29.2% Recall@20。

### 核心洞察
显式负反馈首先反映用户的品类兴趣，其次才是对单物品的厌恶，直接作为负信号建模反而会损失效果。
