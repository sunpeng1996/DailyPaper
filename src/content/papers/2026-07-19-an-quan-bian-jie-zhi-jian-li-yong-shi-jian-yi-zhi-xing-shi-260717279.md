---
title: 'Between Safe Boundaries: Exploiting Temporal Consistency for Jailbreaking
  Text-To-Video Generation Models'
title_zh: 安全边界之间：利用时间一致性实现文本生成视频模型越狱
authors:
- Xingkai Peng
- Jun Jiang
- Jiayang Liu
- Kejiang Chen
- Weiming Zhang
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.17279'
url: https://arxiv.org/abs/2607.17279
pdf_url: https://arxiv.org/pdf/2607.17279
published: '2026-07-19'
collected: '2026-07-26'
category: Multimodal
direction: 多模态生成 · T2V模型越狱攻击
tags:
- Jailbreak
- Text-to-Video
- Temporal Consistency
- MCTS
- Adversarial Attack
one_liner: 提出低查询开销的T2V越狱框架BSB，利用时间一致性实现商用模型攻击成功率相对提升18.6%
practical_value: '- 电商/广告业务上线T2V生成素材功能时，需新增中间帧独立安全审核环节，防范边界无害状态插值生成有害内容的攻击

  - 黑盒场景下做对抗样本/漏洞挖掘，可复用「低成本代理空间MCTS搜索+稀疏高成本空间校准」的范式提升效率

  - 多模态生成服务的安全策略需覆盖时间维度特征，不能仅依赖单帧/单prompt的合规校验规则'
score: 4
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有文本生成视频（T2V）越狱方法多迁移自文生图方案，未利用视频固有时间一致性特性，依赖大量视频查询优化不适用于黑盒场景，对抗prompt搜索缺乏结构化探索策略。
**方法关键点**：提出BSB结构化低查询开销越狱框架，将有害意图编码为两个单独无害的边界状态间的过渡，通过搜索边界状态对使得生成时插值出有害中间帧；采用低成本文本代理空间执行蒙特卡洛树搜索（MCTS），结合稀疏的视频级评估校准结果，大幅降低查询消耗。
**关键结果**：在Veo 3.1、Sora 2、Seedance、Kling v1等主流商用T2V模型上测试，攻击成功率相比最强基线平均相对提升18.6%，验证时间一致性是T2V模型被低估的核心攻击面。
