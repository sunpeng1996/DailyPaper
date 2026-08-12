---
title: 'SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered
  Personal Information'
title_zh: SPIEval：面向分散个人信息场景的移动助手大模型评测基准
authors:
- Junjie Ye
- Zhuohui Sheng
- Shaofan Liu
- Yulun Zhu
- Wenjie Fu
- Dingwei Zhu
- Ming Zhang
- Yujiong Shen
- Weichao Wang
- Xin Zhao
affiliations:
- Fudan University
- Tencent Hunyuan Team
arxiv_id: '2608.10692'
url: https://arxiv.org/abs/2608.10692
pdf_url: https://arxiv.org/pdf/2608.10692
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: Agent 移动端个人信息处理能力评测
tags:
- Mobile Agent
- LLM Evaluation
- Personal Information Processing
- Tool Use
- Benchmark
one_liner: 构建首个跨多App分散个人信息场景的移动助手大模型评测基准，实测顶尖模型准确率仅57.3%
practical_value: '- 开发个人助理类Agent时，可优先优化信息定位能力，79%的失败来自参数匹配错误，可加入检索结果置信度校验机制，低于阈值时触发多轮补充检索，避免过早输出错误结果

  - 若业务中Agent需要对接多个结构化数据源（如电商用户的浏览、收藏、订单、客服多端数据），可参考5维认知能力框架（推理/消歧/整合/偏好推理/多意图分解）拆解任务，定向优化薄弱模块

  - 给Agent设计检索工具时，要引导模型主动使用正则、模糊匹配、字段限定等高级检索能力，实测当前LLM仅2%的检索会用到高级方法，可在prompt中补充工具能力说明和调用示例，大幅提升检索效率

  - 处理多意图用户请求时，即使全量信息给出，当前LLM多意图分解准确率也仅45.7%，可预先对用户query做意图拆分预处理，再分别调用对应模块处理，提升整体准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM移动助手落地时需跨多个App调取分散的个人信息完成用户指令，但现有评测基准要么假设信息明确给出，要么仅支持单文档检索，无法覆盖真实场景下信息分散的核心挑战，导致移动助手的实际能力无法被准确评估。
### 方法关键点
- 构建统一虚拟用户profile，覆盖10类常见App的4335条结构化个人记录，配套21个工具（11个检索工具+10个执行工具），支持多轮交互
- 设计5类核心认知能力评测维度：多跳推理、信息消歧、多源信息整合、用户偏好推理、多意图分解，共包含250个人工标注任务，所有任务经过双人交叉验证，答案可自动校验
- 评测仅校验最终执行工具的调用参数与金标准的匹配度，不要求中间步骤正确，结果客观可复现
### 关键实验
- 测试9款主流SOTA LLMs，最优模型GPT-5.5（xhigh）整体准确率仅57.3%，最弱模型准确率仅16.4%
- 移除检索步骤直接提供全量信息时，平均准确率从35.5%提升至66.8%，79%的失败来自错误的参数取值（即信息定位不准确）
- 仅不到2%的检索调用使用正则、模糊匹配等高级检索方法，98.5%的检索都是基础子串匹配
### 核心结论
当前LLM移动助手的核心瓶颈是分散信息的精准定位能力，模型往往过早输出看似合理的错误信息，而非继续检索验证，这一问题的影响远大于推理能力不足。
