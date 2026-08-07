---
title: 'When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination
  in LLM Agents'
title_zh: 自进化反作用：预提交门控抵御LLM Agent的技能污染
authors:
- Linfang Shang
- Ming Xu
- Yiding Sun
- Tianle Xia
- Lingxiang Hu
- Lan Xu
- Ning Zheng
affiliations:
- Tencent
arxiv_id: '2608.05810'
url: https://arxiv.org/abs/2608.05810
pdf_url: https://arxiv.org/pdf/2608.05810
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 自进化技能管理
tags:
- LLM Agent
- Self-Evolution
- Skill Contamination
- Pre-Commit Gating
- Skill Distillation
one_liner: 提出VaG预提交门控机制，通过三层校验与组合筛选解决自进化Agent不可逆技能污染问题
practical_value: '- 搭建业务自进化Agent（如电商导购Agent、运营自动化Agent）时，不要无条件接入蒸馏生成的技能，必须做前置校验，事后删除污染技能仅能恢复不足20%的性能损失，性价比极低

  - 技能准入校验可直接复用VaG的三层结构：先做零成本结构化字段校验，再用小流量A/B测试单技能对核心指标的影响，最后用低成本LLM调用校验语义冲突/错误，过滤90%以上有害技能

  - 技能批量上线前增加边际增益组合校验：针对电商话术、推荐策略这类可能存在组合冲突的技能，仅选择能提升整体小流量效果的子集上线，避免单独无害的技能组合后降效

  - 经过门控筛选的优质技能库具备跨LLM骨干迁移能力，业务多模型部署时无需重复进化，直接复用即可获得8~16pp的效果提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自进化Agent默认无条件将执行轨迹蒸馏的技能加入运行时上下文，会出现性能先升后降的能力-污染相变：当技能池超过临界规模后，新增缺陷技能不仅直接误导决策，还会成为后续蒸馏的参考上下文，形成跨轮次污染链；且污染具备结构不可逆性，事后删除源技能无法清除后代技能继承的错误逻辑，仅能恢复极少部分性能损失。

### 方法关键点
- 提出Verifier-as-Gatekeeper（VaG）预提交门控架构，新蒸馏技能默认进入Cold层（对运行时不可见），经过两层校验逐步晋升到Warm、Hot层，仅Hot层技能可进入运行时上下文
- Cold→Warm层要求通过三类异构校验：① 结构化校验：确认技能字段符合预设格式；② 行为校验：单技能A/B replay验证不会降低held-out任务性能；③ 语义校验：LLM判断技能无虚假事实、无逻辑冲突、无危险操作
- Warm→Hot层采用边际增益贪心选择：每次加入能最大幅度提升整体held-out性能的技能，仅保留严格正向增益的技能，解决单独无害技能的组合冲突问题

### 关键实验
在Terminal-Bench 2基准上测试：无门控自进化在第3轮达到峰值pass@1 62%，后续降至50%，事后回滚仅恢复2pp性能；VaG实现每轮性能单调提升，第5轮pass@1达72%，技能池规模仅为无门控版本的1/5，效果优于无门控的峰值性能10pp。冻结VaG技能池跨5个不同LLM骨干、跨InterCode NL2Bash基准测试，均获得8~16pp的稳定正向提升。

**最值得记住的一句话：** 自进化Agent的技能准入是前置必须项，而非事后优化选项，预防污染的效果和成本远优于清理污染。
