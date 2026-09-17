---
title: 'PaperDoctor: Evidence-Grounded and Actionable Feedback for Scientific Papers
  in Progress'
title_zh: PaperDoctor：面向待投稿科研论文的有依据可执行反馈Agent框架
authors:
- Kevin Qinghong Lin
- Siyuan Hu
- Pan Lu
- Yu Chen
- Yanzhe Chen
- Owen Queen
- Yupeng Chen
- Jialin Yu
- Junchi Yu
- Zifeng Ding
affiliations:
- University of Oxford
- Stanford University
- National University of Singapore
- University of Washington
- University of Cambridge
arxiv_id: '2609.16995'
url: https://arxiv.org/abs/2609.16995
pdf_url: https://arxiv.org/pdf/2609.16995
published: '2026-09-15'
collected: '2026-09-17'
category: Agent
direction: 科研Agent · 论文质量自动诊断
tags:
- Agent
- Automatic Review
- Evidence Grounding
- Reproducibility
- Scientific Writing
one_liner: 提出三层分级科研论文诊断Agent框架，输出带证据定位与修改建议的投稿前可执行反馈
practical_value: '- 三层分级任务处理架构可直接复用：低成本表层校验先执行，高成本验证/执行类任务按优先级调度，适合电商商品/内容质量审核、推荐策略合规校验等场景，大幅降低算力与人力成本

  - 反馈三元组（问题描述+证据定位+修改建议）的设计可迁移到生成式内容质检：比如电商文案、推荐理由生成的自动纠错，每个问题锚定具体文本片段+明确修改方向，降低人工审核负担

  - 优先级调度思路可用于高计算成本的Agent流程：比如推荐系统AB实验自动复盘Agent，优先验证核心指标正确性，再校验次要维度，在有限预算下最大化收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
AI辅助科研写作与自动科研Agent的爆发导致待投稿论文数量激增、质量不可控，现有自动审稿系统仅输出接收/拒绝的判决类结果，缺乏可落地的修改建议，而人工导师式逐页带定位的反馈成本极高，无法规模化。

### 方法关键点
- 三层分级诊断架构：L1表层筛查低成本校验写作、排版、引文等客观问题，同时提取所有可验证的原子声明；L2分类校验器将声明路由到对应分支，分别完成代码、理论、文献、实验设计校验；L3重现层根据声明重要性与计算预算，优先级重跑实验复现结果
- 所有反馈统一为<问题描述+证据定位+修改建议>三元组，每个问题锚定到具体句子、公式、代码行，可审计且可直接落地
- 实验重现阶段需用户手动确认后执行，避免无效算力消耗

### 关键结果
- 30份待投稿论文的用户调研显示，70.6%的反馈获得作者认可，整体评分全为正，平均得分1.3/2
- 40份跨领域论文对比实验显示，PaperDoctor的反馈100%同时携带证据与修改建议，远高于人类审稿的35.9%、其他Agent审稿的1.5%，覆盖更多人类易忽略的代码、文献维度
- 高优先级实验复现通过率达47.3%，ICML论文复现执行率高但仅14.4%与原文结果匹配

最值得记住的一句话：自动化质量校验的核心不是替代人类做判断，而是把人类的时间从可自动化的核查环节释放出来，聚焦到价值更高的方向性决策上
