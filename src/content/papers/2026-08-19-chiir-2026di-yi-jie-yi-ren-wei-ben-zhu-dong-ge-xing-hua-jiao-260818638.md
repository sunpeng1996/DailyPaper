---
title: Report on The 1st Workshop on Human-Centered Proactive and Personalized Agents
  for Interactive Information Access at CHIIR 2026
title_zh: CHIIR 2026第一届以人为本主动个性化交互信息访问Agent研讨会报告
authors:
- Kirandeep Kaur
- Vinayak Gupta
- Tanya Roosta
- Madhura Raju
- Grace Hui Yang
- Chirag Shah
affiliations:
- University of Washington
- AMD
- UC Berkeley
- TikTok
- Georgetown University
arxiv_id: '2608.18638'
url: https://arxiv.org/abs/2608.18638
pdf_url: https://arxiv.org/pdf/2608.18638
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: 主动交互Agent · 以人为本设计评估
tags:
- Proactive Agent
- Personalization
- Human-Centered AI
- Interactive Information Access
- Evaluation
one_liner: 汇总主动个性化交互信息访问Agent领域共识，明确以人为本设计与评估核心方向
practical_value: '- 电商/内容场景的主动推荐Agent设计需引入「干预校准机制」，按场景风险、用户意图匹配度、干预可逆性分层决策，避免盲目提升主动推送频率打扰用户

  - 主动Agent的评估不要仅依赖点击率、转化率等短期指标，新增干预时机合理性、用户可控性、长期留存/信任度等维度，避免短期收益损害长期用户价值

  - 用户长短期记忆模块设计需增加边界管控能力，支持用户手动删除记忆、关闭个性化记忆、查看记忆来源，降低用户隐私顾虑

  - 主动推送的内容需配套轻量解释入口，说明「为什么现在推荐」，同时提供一键屏蔽同类主动干预的入口，提升用户感知可控性'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前交互信息访问范式已从传统被动查询响应转向Agent主动服务模式，系统可保留跨会话上下文、推断用户潜在需求、主动发起支持，大幅提升了信息获取效率；但现有设计普遍过度关注自动化能力提升，忽略了干预时机不当、过度个性化偏离用户真实需求、用户控制权缺失、评估维度单一等问题，可能导致用户被打扰、隐私泄露、信任受损等负面影响，亟需建立统一的以人为本的主动Agent设计与评估框架。
### 方法关键点
- 重新定义「主动性」为校准后的干预权，而非更早、更频繁的系统动作，需结合干预时机、决策置信度、场景风险、用户意图匹配度做分层决策
- 长短期记忆模块需增加边界管控机制，支持记忆更新、遗忘、来源追溯、用户手动管控，平衡个性化效果与隐私风险
- 主动干预需配套可解释与可抗辩机制，提供「为什么此时干预」的轻量解释、干预等级调节入口、拒绝/修正干预的操作路径
- 评估体系需超越传统准确率、相关性、任务完成率指标，新增干预合理性、时机匹配度、透明度、用户认知负担、长期影响等维度
### 核心共识
本报告为跨领域研讨会成果汇总，无原生对照实验，核心结论来自信息检索、推荐系统、HCI、AI伦理等多领域参会者的研究与实践经验，最终明确了6项未来研究优先级方向，覆盖干预决策建模、评估体系搭建、记忆边界设计、知识 gap 引导、可解释性落地、长期影响追踪等维度。
### 最值得记住的结论
主动性不是系统自动化能力的提升，而是需要被校准的干预权，必须在合适的时机、以合适的方式提供，且始终保留用户的控制权。
