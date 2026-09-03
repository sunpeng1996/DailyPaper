---
title: 'AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on
  Agentic Tool-Calling'
title_zh: AgentJudgeBench：面向智能体工具调用的LLM评委多难度评测基准
authors:
- Abhigya Verma
- Amit Kumar Saha
- Seganrasan Subramanian
- Sai Harshitha Aluru
affiliations:
- ServiceNow AI
arxiv_id: '2608.26623'
url: https://arxiv.org/abs/2608.26623
pdf_url: https://arxiv.org/pdf/2608.26623
published: '2026-08-26'
collected: '2026-09-03'
category: Eval
direction: LLM评测 · 智能体工具调用
tags:
- LLM-as-judge
- Agent
- Tool Calling
- Benchmark
- Evaluation
- DAG
one_liner: 首个面向智能体工具调用场景的LLM评委评测基准，覆盖多难度多拓扑给出选型指导
practical_value: '- Agent工具调用评测选型参考：有ground truth优先选QwQ-32B，无ground truth用GPT-5.4/Gemini-2.5-Pro，要求和人类对齐选GPT-OSS-120B

  - 评测prompt优化优先用结构化分指标rubric，最高提6.5pp对齐率，无需浪费算力调整judge温度、加CoT，二者影响均小于0.3pp可忽略

  - 避坑：不要盲目给GPT-5.4、Gemini-2.5-Pro喂ground truth，会出现过锚定，对齐率反而降1.5~3.9pp

  - 无ground truth的硬任务场景不用纠结选大模型评委，所有模型均卡在77~82%天花板，差异不超过2pp，优先选性价比更高的中小模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM-as-judge已广泛用于评估智能体工具调用系统，但现有评测主要针对开放文本或偏好打分，结构化依赖驱动的工作流场景下评委可靠性完全未被系统验证，从业者缺乏选评委、调配置、解读结果的科学依据。

### 方法关键点
- 数据集：3808条BFCL格式样本，覆盖6种企业级常见DAG拓扑（线性、扇入、扇出、菱形等）、3个难度层级，每条样本都有程序验证的ground truth执行轨迹
- 评测协议：配对设计有/无ground truth两种场景，从工具选择、参数结构、序列准确率、Query覆盖4个正交维度打分
- 实验配置：5个生成器（3B~70B开源模型+GPT-5.4）、6个评委（20B开源到前沿闭源模型）全交叉实验，产出321648组有效评测对

### 关键结果
- 无ground truth时评委对齐率随难度下降速度是有ground truth的1.5倍，硬任务无ground truth场景下所有评委对齐率收敛到77~82%的结构天花板，与模型规模无关
- 结构化评分rubric是最大提分杠杆，对齐率提升4.8~6.5pp，而CoT推理、温度调整影响均小于0.3pp可忽略
- 有ground truth时QwQ-32B对齐率最高，无ground truth时前沿大模型仅领先不到1pp，性价比差异极小
- 前沿模型存在过锚定问题：暴露ground truth反而导致GPT-5.4对齐率降1.5pp、Gemini-2.5-Pro降3.9pp

**最值得记住的一句话**：无ground truth的硬工具调用评测存在能力天花板，盲目堆大模型规模不如优化prompt结构性价比高
