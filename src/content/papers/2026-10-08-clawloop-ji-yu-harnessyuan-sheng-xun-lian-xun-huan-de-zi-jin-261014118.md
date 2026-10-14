---
title: 'ClawLoop: Self-Improving Agents via Harness-Native Training Loop'
title_zh: ClawLoop：基于harness原生训练循环的自进化Agent框架
authors:
- Hansi Yang
- Linji Hao
- Hongyan Hao
- An Wang
- Han Wu
- Qi Gu
- Xunliang Cai
affiliations:
- Meituan, China
- Peking University
arxiv_id: '2610.14118'
url: https://arxiv.org/abs/2610.14118
pdf_url: https://arxiv.org/pdf/2610.14118
published: '2026-10-08'
collected: '2026-10-14'
category: Agent
direction: Agent自进化 · 无教师闭环训练
tags:
- Self-Improving-Agent
- Harness-Agent
- Closed-Loop-Training
- Teacher-Free-Training
- Task-Synthesis
one_liner: 提出无需外部教师的harness原生闭环自进化Agent训练框架，实现任务合成-训练-诊断自主迭代
practical_value: '- 任务合成的双路线+难度控制+两阶段校验方案可直接复用在电商垂类Agent（客服、运营工具、商品运营Agent）的训练数据生成，无需依赖大模型教师做标注，大幅降低训练数据成本

  - 自蒸馏SFT+GRPO的训练范式可迁移到轻量化垂类Agent训练：复用成功轨迹做SFT、同任务多rollout计算组内相对优势做RL，小模型也能获得明显效果提升

  - 失败轨迹自动诊断→定向生成训练任务的闭环逻辑，可直接迁移到推荐系统的badcase自动迭代流程：自动挖掘召回/排序badcase根因，生成对应训练样本，实现模型自主迭代优化'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有harness类Agent的训练流水线依赖外部强教师模型生成任务与轨迹，为单次训练无反馈模式，能力上限受教师模型约束，无法覆盖harness环境下开放的文件操作、shell调用、多步推理等复杂任务场景，缺乏自主迭代能力。
### 方法关键点
- 三阶段闭环框架：任务合成→训练→诊断反馈全程在同一harness沙箱运行，无外部教师依赖
- 任务合成采用双路线：能力驱动合成（通用工作流程跨域实例化，可执行生成器产出带校验规则的任务）+ 领域接地合成（基于领域工具集的技能聚类生成结构化任务），配套诊断驱动的难度增长（多跳结构、噪声注入）+ 两阶段校验，仅保留难度适中（当前Agent通过率1/8~5/8）的任务
- 训练阶段：成功轨迹自蒸馏SFT（环境观测token掩码，仅计算Agent动作损失）+ GRPO强化学习（同任务多rollout组内计算相对优势）
- 诊断阶段：自动分析失败轨迹根因与缺失能力，聚合为诊断报告指导下一轮任务合成
### 关键结果
基于Qwen3.6-27B跑3轮迭代，对比base与ClawGym基线：SkillsBench提升10.9pp（46.3→57.2），Claw-Eval-Live提升7.6pp（69.3→76.9），ClawGym-Bench提升0.8pp（67.6→68.4）；生成的任务迁移到Qwen3.5-4B/9B，效果均优于依赖外部教师的ClawGym训练结果，4B模型Claw-Eval-Live得分从36.8提升至48.0。
### 核心结论
无教师自进化的核心是让Agent自主识别短板、生成针对性训练任务，闭环迭代的效果可超过依赖外部强教师的单次训练模式。
