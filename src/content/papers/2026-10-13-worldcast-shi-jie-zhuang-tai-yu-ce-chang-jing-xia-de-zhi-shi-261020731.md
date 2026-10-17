---
title: 'WorldCast: Exploring Intelligent Visual Generation in World State Prediction'
title_zh: WorldCast：世界状态预测场景下的智能视觉生成探索
authors:
- Wenhao Yan
- Haodong Li
- Xiaotong Li
- Yaxin Luo
- Zhengrong Yue
- Jialv Zou
- Xu Huang
- Haojin Yang
- Nan Jia
- Yan Feng
affiliations:
- THU
- Meituan LongCat
- CUHK
- PKU
- MBZUAI
arxiv_id: '2610.20731'
url: https://arxiv.org/abs/2610.20731
pdf_url: https://arxiv.org/pdf/2610.20731
published: '2026-10-13'
collected: '2026-10-17'
category: Multimodal
direction: 多模态生成 · 世界状态预测基准构建
tags:
- Multimodal Generation
- World State Prediction
- Visual Generation
- Benchmark
- LMM Evaluation
one_liner: 提出4层级视觉生成能力框架，搭建多步世界状态预测基准WorldCast，完成12款主流模型测评
practical_value: '- 可复用其4层级视觉生成能力分层框架，对齐电商商品配图生成、试穿效果预测等多模态生成任务的能力定级，明确迭代优先级

  - 多步状态预测的评测思路可迁移到电商Agent动态决策效果验证，比如用户交互后页面/商品展示变化的仿真测试

  - 实测结论显示多模态生成效果与底层LLM能力强相关，做多模态推荐/Agent时优先选型强基座LLM可降低上层优化成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态生成系统已实现多模态上下文融合与视觉输出，但高阶动态世界状态预测类任务缺乏统一评测标准，研究探索不足。
### 方法关键点
1. 设计4层级视觉生成能力分层框架，明确多步世界状态预测为L3-L4高阶任务，要求模型融合多模态观测输出连续未来视觉状态；
2. 构建WorldCast评测基准，覆盖8大类共320个人工标注用例；
3. 对12款代表性闭源/开源多模态模型开展统一测评。
### 关键结果数字
- 前沿闭源模型GPT-Image-2.5 System得分72.8，具备初步真实场景视觉状态预测能力；
- 次优闭源模型Nano Banana Pro得分仅42.8，最优开源模型得分仅20.1，在复杂上下文、强推理任务上存在明显缺陷；
- 多模态生成效果与底层基座LLM能力强正相关。
