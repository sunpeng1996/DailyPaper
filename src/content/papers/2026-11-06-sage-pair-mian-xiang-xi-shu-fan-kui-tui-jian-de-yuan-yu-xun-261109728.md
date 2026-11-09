---
title: 'SAGE-PAIR: Source-Pretrained Routed Residual Adaptation for Sparse-Feedback
  Recommendation'
title_zh: SAGE-PAIR：面向稀疏反馈推荐的源预训练路由残差适配框架
authors:
- Weiqing Zeng
- Zida Yang
- Guquan You
- Jiexin Zheng
- Cong Wang
affiliations:
- Southwest Jiaotong University
- Peking University
- Guangzhou University
arxiv_id: '2611.09728'
url: https://arxiv.org/abs/2611.09728
pdf_url: https://arxiv.org/pdf/2611.09728
published: '2026-11-06'
collected: '2026-11-09'
category: RecSys
direction: 推荐系统 · 稀疏反馈增量适配
tags:
- Sparse-Feedback
- Residual-Adaptation
- MoE
- PEFT
- Temporal-Drift
one_liner: 冻结推荐主干前提下，通过源预训练残差+用户路由专家实现极稀疏反馈下的排序提升
practical_value: '- 针对天级流量漂移的小样本更新场景，可直接复用「冻结主干+源预训练低维残差校准」架构，避免全量微调的过拟合与算力浪费，适配成本极低

  - 残差特征设计可直接借鉴：仅用前一窗口的点击/点赞等统计特征作为校正输入，无需学习高维表示，300+参数量即可拿到稳定收益，适合在线快速迭代

  - 轻量化MoE路由方案可落地：基于源用户静态行为画像（类目点击直方图、活跃度）做残差专家软路由，无需额外引入动态特征，工程改造成本极低

  - 可渐进式落地：先上线无路由的PAIR版本拿到大部分收益，再叠加路由模块拿0.2%+的增量收益，有明确降级路径'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统天级更新时普遍面临目标窗口反馈极度稀疏（仅0.05%-1%的标注）的问题，传统全量微调、LoRA/Adapter等通用PEFT方法均在高维参数空间做更新，极少量标签下更新方向无约束，容易过拟合或破坏主干已学好的有效结构，无法稳定拿到收益。

### 方法关键点
- 完全冻结推荐主干，仅新增低维残差模块做校正，最终得分 = 主干原始得分*全局校准系数 + 源统计特征加权得分 + 用户路由残差项
- 两阶段训练：先在上一个相邻源窗口（如前一天）预训练残差模块全部参数，再用目标窗口的稀疏标签做少量步数校准，无需重新学习参数方向
- 新增基于源用户静态画像（类目点击直方图、活跃度）的软路由模块，为不同用户匹配不同残差专家，实现差异化校正，总参数量仅331个

### 关键结果
在KuaiSAR-v2公开数据集上，仅用0.5%的目标窗口反馈：
- SAGE-PAIR(Full)的NDCG@10相对基线提升1.77%，路由模块相比无路由的源预训练PAIR版本额外带来0.25%的相对提升
- 对比同参数量的源预训练LoRA/Adapter，SAGE-PAIR的NDCG@10相对高出3%以上
- 训练耗时仅0.6s（远低于全量微调的22s），推理延迟仅增加160ms左右，符合在线部署要求

### 核心结论
稀疏反馈下的推荐适配效果核心由更新空间的可识别性决定，而非标签数量本身，优先用源窗口预定义低维可解释的校正空间，效果远好于盲目使用通用PEFT方法
