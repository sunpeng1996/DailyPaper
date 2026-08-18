---
title: 'How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100
  Real-World Frontier Research Tasks'
title_zh: 自动科研Agent失效模式分析：100项真实前沿任务的端到端诊断评估
authors:
- Yanlin Fei
- Nazhou Liu
- Xinmiao Yu
- Shaolong Chen
- Lei Li
- Rahul Thapa
- Madalina Ciobanu
- Qingqing Mao
- Ritankar Das
affiliations:
- Prentis AI
- Stanford University
- Titan Holdings
arxiv_id: '2608.14905'
url: https://arxiv.org/abs/2608.14905
pdf_url: https://arxiv.org/pdf/2608.14905
published: '2026-08-13'
collected: '2026-08-18'
category: Agent
direction: Agent 自动科研能力评测与失效诊断
tags:
- Agent Evaluation
- AutoResearch
- Failure Taxonomy
- LLM Agent
- Metacognition
one_liner: 提出首个全流程科研Agent评测基准与失效分类体系，定位核心缺陷为元认知能力缺失
practical_value: '- 做电商全链路运营、个性化内容生成等长链路Agent时，可复用ARFT「阶段+根因」双轴失效归因框架，替代仅看最终转化率的单点评估，快速定位链路瓶颈

  - 可直接复用artifact-aware Agent-as-a-Judge架构做长链路Agent自动评测：结合全链路中间产物（如推荐Agent召回/排序日志、文案生成的检索溯源记录）做对齐校验，避免reward
  hacking，标注一致性比单轮LLM-as-Judge提升~20%

  - 推荐/电商Agent优化优先补元认知闭环：在规划-执行链路后增加强制校验环节，要求生成结果与中间日志交叉核对、检测到关键缺陷自动触发重跑，可覆盖80%+常见浅层失效（如文案与商品属性不符、排序逻辑与目标偏离）

  - 开放域无标准答案任务（如新品营销方案生成、用户舆情归因）可参考过程打分逻辑，不强行对齐固定标准答案，转而评估路径的自洽性与严谨性，避免Agent走捷径凑指标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AutoResearch Agent评测存在三大缺陷：任务范围窄仅覆盖单步科研环节、仅做端点打分无法定位失效根因、失效诊断缺乏系统性且看不到中间产物，无法识别reward hacking等问题，难以支撑Agent长链路能力优化。

### 方法关键点
- 构建AutoResearchEval基准：从5878篇2024年后前沿论文筛选100项跨7个领域的全流程任务，含70个开放探索类、30个目标锚定优化类，覆盖构思、检索、执行、分析、写作、自审6个完整科研生命周期
- 提出ARFT失效分类体系：自底向上归纳45种实证失效模式，按「发生阶段+根因」双轴归类，根因分为事实对齐、认知深度、科研诚信、工程鲁棒性4大类
- 搭建人工校准的artifact-aware Agent-as-a-Judge标注流水线：读取全链路中间产物（代码、日志、中间输出）做失效归因，自带质量校验自修复环

### 关键结果
测试8种harness-模型组合，生成800条完整Agent轨迹；Agent-as-a-Judge与人工标注的Cohen's κ在模式级达0.75、根因级达0.83，远高于单轮LLM-as-Judge的0.53/0.62；92%的失效属于三大认知类问题，最常见的「识别到缺陷但不修正」模式出现率达82.5%，所有模型组合均存在一致的核心缺陷。

### 核心结论
当前Agent长链路任务的核心瓶颈不是单步能力不足，而是缺乏元认知循环——无法校验自身产出和中间证据的一致性、发现问题不修正、不反思路径合理性。
