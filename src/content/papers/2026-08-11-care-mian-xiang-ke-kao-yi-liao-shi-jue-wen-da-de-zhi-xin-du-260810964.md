---
title: 'CARE: Confidence-Aware Reasoning for Reliable Medical VQA'
title_zh: CARE：面向可靠医疗视觉问答的置信度感知推理框架
authors:
- Yuetian Du
- Yucheng Wang
- Zhenyuan Chen
- Luyuan Chen
- Rongyu Zhang
- Jinjian Zhang
- Wei Zhou
- Zhijie Xu
- Ming Kong
- Zhan Zhou
affiliations:
- Zhejiang University
- Ant Group
- University of Michigan
- City University of Hong Kong
arxiv_id: '2608.10964'
url: https://arxiv.org/abs/2608.10964
pdf_url: https://arxiv.org/pdf/2608.10964
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · 置信度校准推理
tags:
- MLLM
- VQA
- Confidence Calibration
- CoT
- GRPO
- Reinforcement Fine-Tuning
one_liner: 提出双阶段置信度感知医疗推理框架CARE，同步优化MLLM的VQA准确率与置信度校准
practical_value: '- 多模态商品问答/生成式推荐场景可复用置信度感知奖励机制，将LLM输出置信度与真实正确性绑定优化，降低幻觉率，提升用户对生成结果的信任

  - 缺少高质量CoT标注数据的冷启动场景，可参考结构化CoT合成方法先完成SFT打底，再搭配RL类方法做二次优化，降低标注成本

  - 推荐系统/Agent的生成模块校准可复用GRPO+自定义奖励的思路，同时提升生成准确率与置信度一致性，避免模型输出过度自信的错误结果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
医疗多模态大模型（MLLM）借助强化微调（RFT）实现CoT推理解决VQA任务时，普遍存在置信度误校准问题：模型表达的确定性与实际诊断准确率存在系统性偏差，严重降低下游使用信任度。
### 方法关键点
双阶段CARE置信度感知医疗推理框架可联合优化准确率与校准效果：
1. 冷启动阶段：生成可扩展的结构化Medical-CoT数据集，支撑监督微调（SFT）
2. 强化微调阶段：采用Group Relative Policy Optimization（GRPO）算法，搭配全新置信度感知奖励（CAR）机制，将模型输出的置信度与诊断正确性绑定到奖励信号中
### 关键结果
在3个医疗VQA基准测试集上取得SOTA诊断准确率，同时预期校准误差（ECE）、幻觉率均为最低，为可信临床决策支持提供基础
