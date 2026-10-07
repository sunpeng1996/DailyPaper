---
title: 'DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks'
title_zh: DAEDALUS：基于自生成任务的Agent记忆冷启动方法
authors:
- Antoine Edy
- Max Conti
- Victor Xing
- Marc-Antoine Allard
- Nawfal Benhamdane
- Gautier Viaud
affiliations:
- Illuin Technology
- CentraleSupélec MICS Laboratory
arxiv_id: '2610.08048'
url: https://arxiv.org/abs/2610.08048
pdf_url: https://arxiv.org/pdf/2610.08048
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 自监督记忆冷启动优化
tags:
- LLM Agent
- Procedural Memory
- Self-supervised Learning
- Task Generation
- Heuristic Validation
one_liner: 双Agent自生成适配难度的任务，构建经连续成功验证的可迁移启发式记忆库，无需标注
practical_value: '- 电商导购/运营自动化Agent冷启动无标注任务时，可复用双Agent自探索生成任务的方案，提前提取环境操作启发式，避免上线后重复出错、拉长推理路径

  - 记忆入库可照搬「失败提取启发式→连续N次成功才准入」的校验逻辑，比直接从轨迹提取记忆的准确率更高，减少无效记忆对推理的干扰

  - 记忆库规模较小时（几十条），直接全量注入初始上下文的效果优于BM25、语义检索，推理成本更低，适合轻量化生产Agent落地

  - 新场景无评估基准时，可将自生成任务作为模型排序代理集，其与官方基准的排序相关性达0.89，可快速完成模型选型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM Agent落地新环境时普遍面临冷启动难题：要么依赖人工编写操作指南，要么需要标注训练任务与验证器，成本高、适配速度慢；无记忆的Agent会重复犯同类错误，推理路径长、成功率低，现有记忆构建方法均依赖标注任务，无法适配无先验知识的全新场景。
### 方法关键点
- 双Agent任务生成：探索者Agent先自主探索环境，生成难度适配求解器能力的可解任务与自然语言成功判定条件，任务过易/过难时自动迭代调整难度
- 启发式有效性校验：求解器每次失败后，提取器从失败轨迹生成通用启发式，求解器携带启发式重试，连续成功3次才将启发式入库，避免随机成功引入无效记忆
- 效率优化：前置环境调研确定任务分布、提炼探索经验为任务设计指南，降低探索成本；最终合并去重所有启发式，测试时全量注入初始上下文
### 关键结果
在AppWorld、τ2-bench、AutomationBench三个Agent基准上，比无记忆基线的平均成功率最高提升15.9个百分点，pass^5最高提升2.2倍，效果与使用标注训练任务的SOTA方法相当，推理成本几乎无增加；生成的启发式支持跨模型家族迁移，不同模型均可获得7.7%~29.3%的成功率提升；自生成任务与官方基准的模型排序Kendall τ达0.89，可直接作为代理评估集。

> 仅靠探索得到的记忆甚至会降低Agent性能，只有经过失败-校验-连续成功验证的启发式才能稳定提升效果
