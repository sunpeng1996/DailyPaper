---
title: 'Agent Plasticity: Measuring Self-Improvement Through Experience'
title_zh: Agent可塑性：通过经验衡量自我提升能力
authors:
- Harman Singh
- Anton Bakhtin
- Rulin Shao
- Gabriel Synnaeve
- Ilia Kulikov
- Rob Fergus
- Sanjeev Arora
- Kurt Keutzer
- Jason Weston
- Anuj Mahajan
affiliations:
- UC Berkeley
- Meta Superintelligence Labs
- University of Washington
- Princeton University
arxiv_id: '2610.08902'
url: https://arxiv.org/abs/2610.08902
pdf_url: https://arxiv.org/pdf/2610.08902
published: '2026-10-05'
collected: '2026-10-09'
category: Agent
direction: Agent自我提升 · 效能评估
tags:
- Agent
- Self-Improvement
- Evaluation
- Plasticity
- LLM-Agent
one_liner: 提出Agent可塑性指标，衡量固定权重模型将经验转化为泛化性能增益的效率
practical_value: '- 固定权重Agent迭代方案可复用：无需微调仅更新工具/策略/记忆等持久化artifact，大幅降低部署后迭代成本，适合电商客服、导购Agent的在线优化

  - 效率评估逻辑可迁移：用「held-out性能增益/单位学习成本」计算迭代ROI，可直接用于推荐系统冷启动、Agent技能迭代的投入产出评估

  - 故障诊断框架可落地：将Agent失败分为无对应artifact、有artifact未复用、复用后仍失败三类，快速定位导购/客服Agent的性能瓶颈

  - 长期运营Agent选型参考：优先选择高可塑性模型，即使初始性能差，长期迭代后效果可能反超初始能力强但可塑性低的模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评估仅测量固定时间点的静态能力，无法衡量其从交互经验中自我迭代的效率，也无法定位迭代过程的瓶颈；而部署后的落地Agent（如电商导购、客服、推荐系统的交互Agent）需要持续从用户反馈中学习，静态评估无法支撑长期迭代的选型和优化。

### 方法关键点
- 固定模型权重，仅通过更新持久化artifact（可执行工具、策略、自然语言记忆等）实现自我提升，消除微调带来的变量干扰
- 定义Agent可塑性：单位学习成本下的held-out场景性能增益，区分分布内（ID）泛化增益和分布外（OOD）迁移增益，同时拟合性能饱和点修正平台期带来的效率偏差
- 提出三层故障归因框架：将决策失败分为无对应artifact、有artifact未检索复用、复用artifact后仍失败三类，精准定位迭代瓶颈

### 关键实验结果
在国际象棋、围棋、Hex、NetHack 4类受控环境测试8款前沿大模型：①GPT-5.6 Sol可塑性最高，达298pp/$1000，虽初始性能低于Claude Opus 4.8但最终效果反超；②Claude Fable 5最终静态性能最高但可塑性仅57pp/$1000，约为前者的1/5；③分布内场景的性能增益仅部分迁移到分布外场景，artifact复用率>94%的高可塑性Agent仍有83%~99%的失败来自artifact质量差或应用不当。

**最值得记住的结论：评估长期运营的Agent不能只看初始静态性能，衡量其将经验转化为泛化增益的效率、定位迭代瓶颈同样重要。**
