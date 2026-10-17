---
title: 'Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows'
title_zh: KOLAB：长周期工作流中人类-Agent协作基准数据集
authors:
- Shirley Anugrah Hayati
- Patricia Anugrah Setiani
- Ruizi Wang
- Zhouyi Li
- Khanh Chi Le
- Young-Jun Lee
- Dongyeop Kang
affiliations:
- University of Minnesota
arxiv_id: '2610.21109'
url: https://arxiv.org/abs/2610.21109
pdf_url: https://arxiv.org/pdf/2610.21109
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: 长周期工作流 · 人-Agent协作基准
tags:
- Human-Agent Collaboration
- Benchmark
- Long-Horizon Workflow
- MLLM
- Dataset
one_liner: 发布覆盖40个职业115小时真实人-Agent协作录屏数据集，基准测试前沿MLLM的协作理解能力
practical_value: '- 电商场景智能客服、运营辅助Agent可复用ADOPT/MODIFY/REJECT三分类标签体系，预测用户对Agent输出的接受度，高REJECT概率时主动追问澄清，降低用户跳出率

  - 协作动态度量指标（burstiness、workflow topology、AI retention rate）可直接用于优化Agent交互策略，降低并行任务分支占比，减少用户协调成本提升满意度

  - 做Agent协作效果自动评估时优先采用「操作录屏+结构化工作流图谱」的模态组合，单独用chat log会漏判用户在对话外对AI输出的拒绝行为，准确率下降7%以上

  - 构建Agent训练的Reward Model时，可引入用户在业务系统的实际操作行为（如修改Agent生成的文案、未采用Agent推荐策略）作为弱监督信号，比用户主动打分成本更低、准确度更高'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Agent基准大多聚焦自主完成任务的能力，完全忽略真实长周期工作流中人类会动态调整目标、干预修正、在对话外使用AI输出的场景，导致基准表现优异的Agent实际协作效果差；且现有协作数据集大多为单领域、无真实全链路工作流录屏，无法支撑相关研究与产品优化。

### 方法关键点
- 构建KOLAB数据集：招募50名覆盖40个职业的专业人士，录制115+小时使用Agent完成真实工作的屏幕录像，标注每步Agent输出的人类反馈（ADOPT直接采用、MODIFY修改后采用、REJECT拒绝），同时采集协作满意度、输出质量的人工打分
- 提出三个可复用的协作动态度量指标：burstiness（交互突发性，衡量人类独立工作多久后调用Agent）、workflow topology（分支率，衡量人-Agent并行任务占比）、AI retention rate（AI输出保留率，衡量ADOPT+MODIFY占总输出的比例）
- 设计两类基准任务：① 预测人类对Agent输出的接受分类；② 预测协作满意度与输出质量，测试前沿MLLM的协作理解能力

### 关键结果
- 前沿模型表现远低于实用门槛：GPT-6在接受度预测任务上F1仅51.3%，协作满意度预测的Spearman ρ仅0.38，其余模型表现更差，甚至打不过多数类基线
- 加长上下文、新增模态收益有限：全量工作流上下文对接受度预测的F1提升最多不超过0.07，单独用chat log会低估REJECT比例7%左右
- 模型存在系统性偏差：多数模型倾向预测ADOPT，55%以上的真实REJECT被误判为ADOPT，满意度预测普遍打高分，无法区分低质协作

最值得记住的一句话：当前前沿模型完全不理解真实工作流中的人-Agent协作，自主任务表现好完全不等于协作效果好
