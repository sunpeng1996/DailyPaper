---
title: 'ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning'
title_zh: ATLAS：保留隐空间关系几何的可靠世界模型规划方法
authors:
- Ke Fang
- Yupu Yao
- Lu Cheng
affiliations:
- Pennsylvania State University
arxiv_id: '2609.36333'
url: https://arxiv.org/abs/2609.36333
pdf_url: https://arxiv.org/pdf/2609.36333
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 世界模型隐空间规划优化
tags:
- WorldModel
- LatentRepresentation
- OODGeneralization
- OptimalTransport
- Planning
one_liner: 提出ATLAS训练目标，同时保留隐空间关系结构与校准全局分布，提升世界模型OOD规划性能
practical_value: '- 做生成式推荐/Agent决策的隐空间正则时，可借鉴WEMReg思路，用1维Wasserstein-2距离匹配高斯分布，比传统有限频率高斯正则更能保留隐空间分布特征，避免表征坍塌的同时不丢失OOD判别能力

  - 若模型存在多阶段表征（如用户/物品Encoder中间特征到最终召回/排序用隐向量），可增加OOD-recovery损失，将上游信息丰富的中间表征的pairwise距离结构迁移到下游任务隐向量，保留OOD样本识别能力

  - 评估OOD场景模型鲁棒性时，可参考本文的k-NN novelty score AUROC指标，无需额外标注即可诊断隐向量的表征退化问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有隐空间世界模型的抗坍塌正则仅约束隐向量的全局统计分布，不关注状态间的相对几何关系，导致Encoder中存在的OOD相关信息在最终规划用的隐向量中被大幅削弱，OOD场景下的规划失败率显著升高。
### 方法关键点
- 提出ATLAS三部分联合训练目标：原有隐空间多步预测损失`L_pred`，搭配新增的WEMReg分布校准损失和OOD-recovery关系保留损失
- WEMReg：随机采样单位方向将高维隐向量投影到1维，通过Wasserstein-2距离匹配标准高斯分布，相比传统有限频率高斯正则可避免分布歧义，更严格地完成全局分布校准
- OOD-recovery：以Encoder输出的均值池化Patch表征为固定锚点，约束规划用隐向量的标准化pairwise距离与锚点一致，保留状态间的相对几何关系和OOD识别能力
### 关键结果
在PushT（机械臂操控）、TwoRoom（2D导航）、OGBench-Cube（3D机械臂操控）三个数据集上对比LeWM等4个基线方法：
- 相比LeWM，ATLAS在ID场景最高提升12.2pp（TwoRoom），OOD场景最高提升19.8pp（TwoRoom）
- 规划隐向量的OOD失败预测AUROC从LeWM的0.44提升至0.75，接近锚点表征的0.77，多步预测误差随rollout步长增加的涨幅显著低于基线
### 核心结论
隐空间的全局分布校准和相对几何结构保留是两个非冗余约束，同时优化二者可大幅提升OOD场景下的规划鲁棒性
