---
title: 'RoSci: Exploring Robustness in Science VLMs'
title_zh: RoSci：科学领域视觉语言多模态模型的鲁棒性探索
authors:
- Junying Wang
- Yijin Guo
- Yalun Wu
- Ziheng Jiao
- Farong Wen
- Qihang Yan
- Wenzhe Li
- Ye Shen
- Qi Jia
- Chunyi Li
affiliations:
- Fudan University
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- Nanyang Technological University
arxiv_id: '2611.27750'
url: https://arxiv.org/abs/2611.27750
pdf_url: https://arxiv.org/pdf/2611.27750
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: 多模态Agent · 鲁棒性评测与优化
tags:
- VLM
- Robustness
- Agent Pipeline
- Benchmark
- Multimodal Reasoning
one_liner: 提出科学VLM鲁棒性定义、RoSci-Bench评测集与前置校验推理的RoSci-Agent框架
practical_value: '- 多模态Agent（如电商商品理解、广告素材审核Agent）可复用Parse-Verify-Decide前置校验pipeline，先校验输入信息的完整性、正确性再推理，降低错误输出率

  - 构建模型鲁棒性评测集时可复用seed-variant策略，基于原始样本生成不同降级类型的变种样本，覆盖真实场景的信息错误、缺失边界case

  - 对输入可靠性不确定的场景（如泛化搜索query理解、UGC内容识别）可引入选择性回答/请求澄清/拒绝回答机制，提升系统整体可靠性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有科学领域VLM默认输入信息完整准确，未考虑真实场景普遍存在的信息错误、缺失问题，易输出不符合事实的不可靠结果，缺乏对应的鲁棒性定义与评测标准。
### 方法关键点
1. 明确定义科学VLM鲁棒性为异常检测、可解性评估、自校准三类核心能力，覆盖信息不一致、信息不足两类典型异常场景
2. 构建RoSci-Bench诊断评测集，包含1220个样本，采用seed-variant生成策略覆盖6种输入降级类型
3. 提出RoSci-Agent框架，采用Parse-Verify-Decide三阶段pipeline，推理前先校验输入前提有效性，支持输出答案、请求澄清、拒绝回答三类决策
### 关键结果
RoSci-Agent的整体鲁棒性得分显著优于所有参评的独立VLM基线，RoSci-Bench为多模态推理社区提供了统一的鲁棒性评测基准。
