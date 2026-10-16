---
title: 'Intern-Decision: Efficient Multimodal Decision Making with Autoregressive
  Masked Language Modeling'
title_zh: Intern-Decision：基于自回归掩码语言建模的高效多模态决策模型
authors:
- Tong Zhu
- Zhe Xu
- Zefeng He
- Yunkai Chai
- Xuyang Hu
- Dehong Zheng
- Yun Luo
- Yafu Li
- Qi Zhang
- Yu Cheng
affiliations:
- Shanghai AI Lab
- Shanghai Jiao Tong University
- Fudan University
- Nanyang Technological University
arxiv_id: '2610.22131'
url: https://arxiv.org/abs/2610.22131
pdf_url: https://arxiv.org/pdf/2610.22131
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 轻量多模态结构化决策
tags:
- Multimodal
- Structured Decision
- Agent
- Low Latency
- Model Calibration
one_liner: 提出轻量多模态决策系列模型，单前向Pass输出结构化决策与概率，精度领先且延迟大幅降低
practical_value: '- 电商/广告系统的结构化分类任务（如客服工单分流、商品打标、用户意图识别）可复用「JSON骨架+单前向pass决策」范式，替代LLM自由生成JSON，降低解码延迟和格式错误率

  - Agent系统的工具调用、动作选择模块可直接复用该轻量决策模型，结合temperature scaling校准置信度，实现低置信度请求路由到大模型的级联架构，平衡精度和成本

  - 多模态交互场景（如直播导购界面动作识别、智能客服视觉工单处理）可复用「视觉塔冻结+语言主干微调」的训练策略，降低多模态决策模型的训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent系统多依赖LLM自由生成完成闭集决策任务，引入额外解码开销，且输出格式不稳定；同时现有结构化决策模型多仅支持文本输入，无法覆盖多模态Agent的视觉感知+决策需求，亟需适配多模态场景的高效结构化决策方案。

### 方法关键点
- 将结构化决策建模为预定义JSON骨架中掩码决策字段的next token预测任务，仅在监督阶段引入真实标签符号，推理时单因果前向pass即可通过原生LM头输出所有字段的候选概率和结构化结果，无需迭代生成
- 构建统一多模态决策语料，覆盖文本推理、指令遵循决策、视觉判断、界面动作等场景，基于Qwen3.5主干训练0.8B/2B/4B三个参数规模的模型，训练时冻结视觉塔和投影层，仅微调语言主干
- 引入post-hoc temperature scaling校准输出概率，基于决策置信度实现模型级联路由，低置信度请求转发更大模型处理

### 关键结果
- 7个测试集上4B模型平均精度90.02%，优于基线Jev v1.13.0的88.74%
- 单RTX4090上289token+3字段请求的平均延迟：4B模型44.16ms，0.8B/2B模型约33~34ms，仅为Jev延迟的1/3左右
- temperature scaling将多类Brier得分从0.628降至0.550，预期校准误差从0.213降至0.089；置信度路由方案在Jevbench-Hard集上将精度从73.87%提升至87.39%，仅调用大模型处理37.8%的请求，耗时比全用大模型降低53%

最值得记住的一句话：轻量结构化决策模型可作为大模型的互补组件，成为Agent系统中低成本、低延迟的本地决策单元
