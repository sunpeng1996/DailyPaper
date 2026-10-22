---
title: 'TraceForge: Distilling with Your Own Thinking'
title_zh: 《TraceForge：基于模型家族原生推理轨迹的合法蒸馏方法》
authors:
- Yan Wang
affiliations:
- Independent Researcher
- ALLE AI Lab
arxiv_id: '2610.29680'
url: https://arxiv.org/abs/2610.29680
pdf_url: https://arxiv.org/pdf/2610.29680
published: '2026-10-20'
collected: '2026-10-22'
category: Training
direction: 大模型蒸馏 · 推理轨迹合成
tags:
- Knowledge Distillation
- Chain-of-Thought
- Adversarial Training
- Reasoning Trace
- LLM Fine-tuning
one_liner: 无需破解闭源模型推理轨迹，生成学生家族原生轨迹实现合规高效蒸馏
practical_value: '- 垂直场景小模型蒸馏可复用该思路：无需对齐闭源大模型的推理风格，用同家族原生推理轨迹做训练，可降低灾难性遗忘，提升query理解、规则推理、客服生成等任务效果，同时规避合规风险

  - 两阶段轨迹生成框架可直接落地：先SFT让生成器学习同家族推理范式，再用判别器做best-of-N筛选，无需人工标注推理步骤，训练成本低

  - 电商Agent微调可参考该范式：将大模型输出的决策结果作为固定输入，生成小Agent同架构的推理轨迹做微调，既能复用大模型决策能力，又能保留小Agent原生响应风格，减少适配成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
闭源大模型当前已停止输出完整推理轨迹，直接破解轨迹的方法违反服务条款无法用于商业产品；传统蒸馏方案直接用异源大模型的推理轨迹训练小模型时，风格差异会导致灾难性遗忘、训练不稳定、效果下降，亟需合法且高效的蒸馏替代方案。
### 方法关键点
- 推理轨迹生成器SFT：基于学生模型家族的公开授权对话数据微调，学习从上下文、答案反推同家族原生推理轨迹的能力，损失仅作用于推理轨迹部分，确保输出是推导过程而非答案复述
- 对抗协同优化：训练同规模判别器区分真实/生成的家族推理轨迹，经过5轮在线对抗迭代优化生成器，推理时用判别器选出4个候选中的最优轨迹
- 全链路合规：生成器、判别器训练数据全部来自学生家族可授权使用的公开数据，仅推理时用闭源大模型的答案作为输入，无闭源数据反向传播环节
### 关键实验结果
固定学生模型为Qwen3.5-9B-Base、训练配方、数据规模不变，对比4种基线方案：
- 用家族原生轨迹替代Fable 5原轨迹，HumanEval+ pass@1提升3.7个点，MBPP+提升7.1个点，训练全程无大幅波动
- 基于GPT-6.1-SOL的答案生成原生轨迹，相比TraceInversion合成轨迹，HumanEval+、MBPP+ pass@1分别提升55.5、53.4个点，无训练崩溃问题
### 核心结论
最好的学生不是由最好的老师单独教出来的，而是由最好的老师用学生最习惯的方式教出来的
