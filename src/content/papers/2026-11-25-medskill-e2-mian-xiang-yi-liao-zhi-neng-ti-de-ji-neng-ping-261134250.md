---
title: 'MedSkill-E$^{2}$: Evaluating and Evolving Skills for Medical Agents'
title_zh: MedSkill-E²：面向医疗智能体的技能评估与进化框架
authors:
- Jingjing Hua
- Shaocong Wei
- Jianghan Shen
- Junzhi Ning
- Min Cen
- Cheng Tang
- Ziyan Huang
- Jiepeng Li
- Fengshuo Liu
- Kangkun Mao
affiliations:
- Shanghai Artificial Intelligence Laboratory
- University of Chinese Academy of Sciences
- Nanjing University
- Imperial College London
- Fudan University
arxiv_id: '2611.34250'
url: https://arxiv.org/abs/2611.34250
pdf_url: https://arxiv.org/pdf/2611.34250
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 技能利用效率优化
tags:
- LLM Agent
- Skill Optimization
- Benchmark
- Medical AI
- Evolutionary Method
one_liner: 提出技能使用不足（EBU）量化方法、对应基准EBU-Bench与进化方案EBU-Evolve，提升Agent自主技能使用准确率
practical_value: '- 技能评估可复用EBU量化思路：对比「Agent自主使用技能」和「强制引导使用技能」的效果差，定位当前技能描述、唤起逻辑的缺陷，适合电商导购Agent的优惠券计算、规则匹配类技能的gap排查

  - 技能迭代可复用干预到指令蒸馏流程：用同任务下「自主执行失败、引导执行成功」的配对轨迹，仅修改技能的描述/正文文本，无需调整模型参数即可提升技能效果，适配固定技能库的低成本迭代

  - 优先优化技能描述可快速获增益：实验显示仅修改技能描述就能拿到85%以上的联合优化收益，同时提升技能唤起率，业务中可先迭代技能的触发条件、适用场景描述，快速拿到效果提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent依赖预置技能完成复杂任务，但普遍存在「技能已挂载但自主执行时未充分利用（EBU）」的问题，尤其在高风险领域错误应用技能会产生严重后果；现有评估仅对比有无技能的差异，无法量化技能的未利用程度，也缺乏低成本的技能优化方案。

### 方法关键点
- 构建EBU-Bench基准：覆盖12类医疗任务共331个任务-技能对，定义EBU gap为「强制引导使用技能的准确率」减去「自主使用技能的准确率」，量化未利用的收益空间
- 提出EBU-Evolve进化方法：用同任务下自主执行、引导执行的配对轨迹，蒸馏优化技能的描述与正文，仅修改技能文本不调整模型参数，优化后经验证选优，可跨模型、跨执行框架迁移

### 关键结果
在154任务的EBU-Bench Lite上测试9个主流LLM+2个执行框架的组合，平均EBU gap达43.94pp，同一模型跨框架的自主技能使用准确率差最高达38.96pp；EBU-Evolve优化后，自主技能使用准确率提升33.33~55.17pp，跨模型/框架迁移仍有16.09~50.57pp的提升，效果远超GEPA、SkillOpt等现有优化方法。

**最值得记住的一句话**：仅给Agent挂载技能不足以释放其价值，技能的描述清晰度、唤起引导设计对实际使用效果的影响，甚至超过模型本身的能力差异
