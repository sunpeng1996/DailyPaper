---
title: 'GEPA-Curator: Curated Learning for Self Improving Agents'
title_zh: GEPA-Curator：面向自进化Agent的精选学习框架
authors:
- Zack Yu
- Nicholas Lee
- Minjae Lee
- Lakshya Agarwal
- Luca Manolache
- Wonjun Kang
- Matei Zaharia
- Michael W. Mahoney
- Kurt Keutzer
- Sehoon Kim
affiliations:
- UC Berkeley
- ICSI
- LBNL
- Furiosa AI
- KAIST
arxiv_id: '2610.37651'
url: https://arxiv.org/abs/2610.37651
pdf_url: https://arxiv.org/pdf/2610.37651
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent自进化 · 反射式Prompt优化
tags:
- LLM Agent
- Prompt Optimization
- Self Improvement
- Curriculum Learning
- Trajectory Retrieval
one_liner: 通过任务精选和过往成功轨迹检索提升Agent反射式Prompt优化的性能和可靠性
practical_value: '- 做电商导购Agent、推荐系统Agent自优化时，可先对训练任务做筛选，过滤环境故障、任务不可行、评估噪声导致的无价值失败样本，避免Prompt被错误修正，比如加购失败如果是页面bug就不要归因为Agent指令问题

  - 反射式优化Agent Prompt时，可搭配历史成功轨迹做对比学习，给Reflector提供明确的参考基准，比如同样的商品查找任务之前跑通的路径和现在失败的路径对比，快速定位问题点，比仅靠失败轨迹猜修复方案效果好

  - 成本敏感的业务场景可复用高效版Curator的优化技巧：设置任务跳过周期、旧轨迹用精简摘要存储、仅保留一条最优成功轨迹，在几乎不损失效果的前提下降低额外调用成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有反射式Prompt优化方法默认所有Agent执行失败轨迹都能提供有效学习信号，但实际多轮交互场景下，失败可能来自环境故障、工具不可用、评估噪声、任务本身不可行等非Prompt原因，直接用这些噪声样本优化会引入错误的Prompt修改，反而降低Agent性能。
### 方法关键点
- 任务精选模块：基于每个任务的历史执行轨迹动态筛选训练batch，跳过已稳定成功、多次失败来自非Prompt因素、评估结果反复波动的任务，仅保留能提供有效优化信号的任务，且跳过是临时的，每轮训练会重新评估是否重新纳入
- 历史成功轨迹检索模块：对当前batch中的失败任务，检索同任务过往稳定成功的轨迹作为上下文输入给Prompt优化器，让Reflector通过对比失败和成功轨迹定位问题，无需盲目猜测修复方案
### 关键实验
在WebArena（含电商购物等4个场景）、ALFWorld、AppWorld、τ-bench共4类Agent基准上测试，对比GEPA、ACE两个基线：
- 用Gemini 3.1 Pro做优化器时，相对GEPA最高提升20.7%，相对ACE最高提升21.2%；用Claude Opus 5做优化器时Prompt优化增益是GEPA的1.78倍
- 高效版Curator仅增加31%的优化成本，就能获得3.6%~18.5%的准确率提升，非WebArena场景下成本仅为ACE的1/4.42，准确率反而高9.2%
### 核心结论
Agent自进化的关键瓶颈不是优化算法本身，而是输入优化器的学习信号质量，过滤噪声样本+提供对比参照的收益远高于单纯迭代优化策略
