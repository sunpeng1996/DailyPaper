---
title: 'LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL'
title_zh: LLM-as-a-Tutor：面向不可验证强化学习的策略感知提示适配框架
authors:
- Yujin Kim
- Namgyu Ho
- Sangmin Hwang
- Joonkee Kim
- Yongjin Yang
- Sangmin Bae
- Seungone Kim
- Jaehun Jung
- Se-Young Yun
- Hwanjun Song
affiliations:
- KAIST
- Upstage
- University of Toronto
- Carnegie Mellon University
- NVIDIA
arxiv_id: '2607.04412'
url: https://arxiv.org/abs/2607.04412
pdf_url: https://arxiv.org/pdf/2607.04412
published: '2026-07-04'
collected: '2026-07-09'
category: Training
direction: 大模型对齐 · 策略感知训练提示动态优化
tags:
- Reinforcement Learning
- RLHF
- Prompt Adaptation
- Curriculum Learning
- GRPO
one_liner: 通过单LLM兼任裁判与导师，动态调整训练提示难度，解决不可验证RL的奖励信号缺失问题
practical_value: '- 做LLM对齐/Agent训练时，可直接复用这套难度动态适配逻辑：当当前训练任务的reward方差低于阈值时，优先给prompt追加细粒度约束，比优化评分规则能更快恢复奖励信号的区分度，避免训练停滞

  - 生成类任务（电商文案、客服话术、广告创意）的RL训练中，优先用append方式修改prompt而非整体重写，既保证难度单调上升，又不会偏离原始业务场景的任务分布，训练稳定性更高

  - 做效果判别时，优先用pairwise两两对比而非单点打分，LLM的判断准确率更高，可复用这套逻辑快速识别当前任务对模型的适配程度，不需要人工标注难度等级

  - 电商场景下的Agent训练可直接套用框架：比如客服话术训练时，当模型都能正确回复基础咨询，自动追加"提及当前满减活动""引导用户加入会员"等约束，逐步提升模型的业务适配能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前不可验证RL（如开放域指令遵循、文案生成）依赖带细粒度评分规则的LLM裁判作为奖励信号，但现有方法的训练提示均来自固定语料，极易出现提示难度与模型能力不匹配的问题：要么提示太简单所有模型输出都达标，要么太难所有输出都不达标，导致LLM裁判无法生成有区分度的奖励信号，训练陷入停滞，仅优化评分规则无法解决该问题。

### 方法关键点
- 提出LLM-as-a-Tutor框架，复用同一LLM同时担任考官和生成器：考官通过pairwise对比当前策略的两个输出，判断当前提示是否有区分度；若没有区分度，生成器给提示追加原子约束，同时对应更新评分规则，保证难度单调上升
- 采用append-only的提示修改方式，不改动原始提示内容，仅追加约束，既保证难度只升不降，也不偏离原始任务分布
- 每轮训练迭代都重新检查所有提示的区分度，自动适配当前模型能力，无需人工设置难度调度规则

### 关键实验
用Qwen3-1.7B作为训练策略，Qwen3-8B作为导师/裁判，在FollowBench、AdvancedIF、InfoBench三个指令遵循基准上测试，对比固定提示、Evol-Instruct、EVA等7个基线，平均得分51.96，比次优基线高0.92分，在6个细分指标中5个排名第一。消融实验显示append方式比重写提示平均高0.31分，策略感知的约束添加比随机加约束平均高0.37分。

### 核心结论
提示难度与模型能力的匹配度，是比评分规则更核心的奖励信号质量决定因素，调整提示本身是不可验证RL训练中被忽略的关键优化维度。
