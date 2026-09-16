---
title: 'ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific
  Agents'
title_zh: ScienceBuddy：面向交互式科研Agent的嵌套递归自改进框架
authors:
- Shuhan Xue
- Jianyuan Zhong
- Ziyuan Nan
- Wenbin Li
- Zhaochen Yu
- Jinchao Ding
- Qiang Gao
- Pengyu Zhan
- Yuntong Zhang
- Tian Cheng
affiliations:
- PhAI Labs
arxiv_id: '2609.17523'
url: https://arxiv.org/abs/2609.17523
pdf_url: https://arxiv.org/pdf/2609.17523
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: Agent自迭代 · 递归协同优化
tags:
- Agent Self-Improvement
- Recursive Optimization
- GRPO
- LLM Agent
- Rubric Reward
one_liner: 提出嵌套递归自改进范式，实现Agent执行流程与模型的协同持续进化
practical_value: '- 可复用嵌套递归迭代框架：固定模型先迭代prompt/工具调用流程（对应inner recursion），再固定流程做RL调优模型，降低业务Agent迭代的调参复杂度，减少线上波动

  - 可借鉴用户交互转训练信号的流程：把用户对Agent的反馈、执行轨迹自动转成任务评估rubric和训练样本，无需额外人工标注就能实现持续迭代，适合电商导购Agent、客服Agent的闭环优化

  - 可复用rubric reward + GRPO的训练范式：针对业务自定义的多维度评估规则自动生成奖励信号，比人工标注偏好数据成本低，适配推荐/广告场景的多目标优化需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有交互式Agent仅能在单次对话中修正输出，无法将用户协作反馈转化为跨任务的通用能力提升，单独优化prompt执行流程或模型参数的范式难以实现能力的长期持续迭代，也无法保证迭代过程中线上服务的稳定性。
### 方法关键点
- 嵌套递归自改进范式：inner recursion固定任务模型，用固定辅助模型诊断执行失败点，对harness（包含prompt、技能库、上下文管理逻辑）做小范围单维度修改，仅保留验证集得分正向提升的修改；outer recursion固定最优harness，基于交互生成的带rubric标注任务做GRPO强化学习更新模型参数
- 交互信号自动转化pipeline：将用户请求、交互轨迹、反馈自动打包为包含任务指令、输入资产、执行环境、评估rubric的Harbor任务，可同时支撑SFT和RL训练
- 异步迭代机制：后台迭代harness和模型时不中断线上服务，更新后经过重评估再上线，所有历史版本harness和任务环境均留存复用
### 关键结果
在LAB-Bench、Biomni-Eval覆盖的4类科研任务（文献阅读、数据库查询、协议排障、基因变异评估）上测试：3轮嵌套迭代后整体测试准确率从42.2%提升至73.3%；固定模型仅迭代harness，验证集准确率提升20个百分点；固定harness仅做RL训练，问题覆盖度（pass@4）提升19.5个百分点。

最值得记住的一句话：Agent的持续迭代不需要盲目堆数据，通过流程优化和模型训练的解耦协同，可用更低成本实现能力的稳步提升。
