---
title: 'XStack: A Benchmark for ML Repo Migration'
title_zh: XStack：机器学习代码仓库跨生态迁移评测基准
authors:
- Linrong Cai
- Taiming Lu
- Haozhe Chen
- Zhuang Liu
affiliations:
- Princeton University
arxiv_id: '2611.08472'
url: https://arxiv.org/abs/2611.08472
pdf_url: https://arxiv.org/pdf/2611.08472
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 跨生态代码迁移能力评测
tags:
- Agent
- Benchmark
- Code Migration
- LLM
- Evaluation
one_liner: 推出针对ML仓库跨PyTorch/GPU到JAX/TPU迁移任务的Agent能力评测基准
practical_value: '- 开发代码迁移类Agent时，可直接复用XStack的评测数据集与校验逻辑，避免自行构造迁移任务的成本

  - 推荐团队做跨框架模型迁移（如PyTorch召回模型转JAX部署TPU）时，可参考其基于原模型效果对齐的校验规则，搭建自动化迁移验证流程

  - 长链路Agent业务选型时可参考其成本-效果结论：高准确率Agent开销显著更高，可按业务容忍度平衡迁移成功率与调用成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前ML代码高度绑定PyTorch/NVIDIA GPU、JAX/Google TPU两大生态，跨生态手动迁移成本极高，且缺乏标准化基准衡量Agent完成这类长链路复杂工程任务的能力。
### 方法关键点
XStack基准设定任务为：Agent接收PyTorch GPU仓库，在空白TPU环境中输出可运行的JAX版本代码，通过标准为迁移后代码的实验效果与原仓库公开结果对齐，覆盖代码理解、改写、编译、效果验证全流程。
### 关键结果数字
当前主流Agent迁移效果仍不稳定：Claude Opus 5通过率最高为75%，GPT-5.6-sol通过率45%，其余Agent通过率不超过40%；迁移通过率与Agent调用成本正相关，可基于Pareto前沿做成本与效果的权衡。
