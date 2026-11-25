---
title: 'RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis'
title_zh: RecordRoute：基于定位引导诊断的多Agent故障审计方法
authors:
- Yifan Duan
- Lihuan Li
- Chao Xue
- Siyuan Zheng
- Du Yin
- Flora D. Salim
affiliations:
- UNSW Sydney
arxiv_id: '2611.33022'
url: https://arxiv.org/abs/2611.33022
pdf_url: https://arxiv.org/pdf/2611.33022
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: Agent故障归因 · 定位诊断
tags:
- Agent Failure Attribution
- Pairwise Ranking
- Local Diagnosis
- TF-IDF
- Multi-Agent
one_liner: 提出结合轨迹内成对排序与局部诊断的Agent故障归因方法，性能全面优于现有SOTA
practical_value: '- 电商/广告多Agent协作系统（如智能客服、投放优化Agent集群）可直接复用该架构：先定位最早出错的步骤与责任角色，再仅基于该步骤文本诊断错误类型，相比全轨迹诊断准确率提升8个百分点，同时降低计算成本

  - 轨迹内步骤排序任务优先选用word+char级TF-IDF特征叠加成对损失，比常用的dense embedding方案效果高17个百分点以上，特征提取与训练成本极低，适合业务侧轻量级故障归因工具快速落地

  - 推断时仅需对每个步骤单独打分排序，单轨迹CPU推断时延仅9.32ms，适合线上多Agent服务的实时故障告警、自动熔断场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent/多Agent系统执行长链路任务时，出错后仅能观测到最终失败结果，难以定位最早的责任角色、根因步骤与错误类型；现有方法要么仅做步骤定位，要么基于全轨迹表征预测归因目标，容易把错误传播的后续症状判定为根因，全轨迹诊断还会混入大量无关信息，降低错误模式识别准确率。

### 方法关键点
- 步骤特征融合word 1-2gram + char 3-5gram的TF-IDF特征，叠加步骤文本与任务query的重叠特征，保留工具名、异常片段、操作话术等细粒度文本线索，避免dense embedding丢失 lexical 匹配信息
- 定位模块采用轨迹内正负样本成对排序损失训练，仅比较同一条失败轨迹内的步骤差异，推断时直接给每个步骤打分，选择得分最高的最早步骤，输出对应的责任角色与步骤坐标
- 错误模式诊断仅基于定位到的单步骤文本、结构元数据与角色信息，无需输入全轨迹内容，避免后续传播的错误信息干扰诊断结果

### 关键结果
在Who&When Pro、TraceElephant、CatchBench三个公开基准上测试，对比StepFinder、ASCon等SOTA监督模型及Qwen2.5-14B、Mixtral-8x7B等开源LLM：
1. Who&When Pro上联合准确率达77.47%，比全轨迹诊断高8.19个百分点，比ASCon高11.37个百分点
2. TraceElephant自然故障数据集上步骤准确率达27.06%，比ASCon高8.25个百分点
3. CatchBench POST场景下Top-1准确率37.46%，MRR达0.590，均为所有对比方法最优

### 核心结论
Agent故障归因时先定位根因步骤再基于单步内容诊断，比直接用全轨迹分析的效果更好、计算成本更低
