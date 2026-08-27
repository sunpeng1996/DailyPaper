---
title: 'MARS: Multi-Specialist LLM Relay System for Competitive Programming'
title_zh: MARS：面向竞赛编程的多专长大模型接力系统
authors:
- Andrei Mikhailov
- Mikhail Burtsev
- Alsu Sagirova
affiliations:
- MIRAI
- London Institute for Mathematical Sciences
- AXXX
arxiv_id: '2608.23918'
url: https://arxiv.org/abs/2608.23918
pdf_url: https://arxiv.org/pdf/2608.23918
published: '2026-08-23'
collected: '2026-08-27'
category: Agent
direction: 多智能体 · 领域专长协作优化
tags:
- Multi-Agent
- Code Generation
- RAG
- LLM
- Pipeline Optimization
one_liner: 提出纯prompt的领域专精多智能体接力框架，竞赛编程准确率较直接提示提升14.4个百分点
practical_value: '- 多智能体分工可放弃通用的规划/执行/校验角色拆分，按业务垂直领域（如推荐召回/排序/冷启动、电商类目/营销/履约）拆分专精Agent，每个Agent绑定对应领域知识库的RAG做知识grounding，分工匹配更精准

  - 接力协作流程中引入每步可观测的业务校验信号（如推荐预估CTR、搜索相关性分）做Agent的保留/修复/移交决策gate，避免无效迭代，大幅降低token消耗

  - 纯prompt+动态选队的机制无需调整大模型权重，业务侧可快速落地，改造成本低ROI高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体代码生成方案普遍采用通用的规划/编码/调试角色拆分，完全依赖大模型预训练的通用能力，没有针对性注入垂直领域专业知识，在竞赛编程这类需要深度算法知识的复杂任务上准确率低、推理成本高、结果波动大。

### 方法关键点
- 每个Agent为单一算法领域（动态规划、图论、字符串、几何等）的专精角色，各自绑定对应算法语料的RAG做知识grounding
- 任务触发后先由所有专精Agent自我评估匹配度，筛选最多3个最相关的Agent组成临时团队，投票选出初始编写Agent
- 接力流程每步执行两次LLM调用：第一次生成/修改代码，在沙箱运行公开用例得到执行报告；第二次基于报告决定保留代码/修复/移交下一个Agent，修复后的代码要求不能低于当前版本的公开用例通过率
- 最后增加基础设施修复Agent，仅处理IO、头文件等模板类错误，不修改核心逻辑

### 关键实验
在CodeContests测试集165道题上测试，backbone采用Gemma 4，对比直接提示、单专精RAG、并行集成、基础接力等baseline：MARS通过率达0.624±0.006，较直接提示高14.4个百分点，较SOTA的CodeSIM低10.7个百分点但推理耗时仅为后者的1/3.3，单任务token消耗的标准差小7倍。

**最值得记住的结论**：将多智能体的角色拆分从流程分工改为领域分工，配合每步可观测的校验信号，能以极低的成本大幅提升复杂专业任务的解决效率。
