---
title: A team of Gemini 4 Argon agents beats Minecraft
title_zh: Gemini 4 Argon多智能体团队从零通关《我的世界》击败末影龙
authors:
- Maxence Faldor
- Satinder Singh
- Roberta Raileanu
affiliations:
- Google DeepMind
arxiv_id: '2610.22319'
url: https://arxiv.org/abs/2610.22319
pdf_url: https://arxiv.org/pdf/2610.22319
published: '2026-10-14'
collected: '2026-10-16'
category: MultiAgent
direction: 多智体协作 长周期开放世界任务落地
tags:
- MultiAgent
- LLM-Agent
- Embodied-Agent
- Long-Horizon-Task
- Code-as-Policy
one_liner: 4个通用Gemini 4 Argon编码智能体无人类干预27小时通关《我的世界》击败末影龙
practical_value: '- 多智能体无预定义角色自主分工机制，可复用在电商大促跨链路Agent调度场景，自动协商分配运营/供应链/流量端子任务，无需人工预设职责边界

  - 共享记忆+失败自动复盘沉淀规则的机制，可迁移到推荐/广告系统线上故障自愈，出错后自动根因分析并更新全团队执行规则，避免重复踩坑

  - 91% KV cache 复用降本的经验，可用于LLM驱动的用户运营/客服Agent集群，高频场景复用历史上下文，token成本可降低80%以上

  - 独立Observer智能体无干预校验的架构，可用于广告投放/内容推荐Agent的合规巡检，全程自动识别违规操作，降低人工审核成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有开放世界长周期智能体方案多依赖预训练游戏策略、人类编写的专用工具库，或仅支持单智能体执行短周期任务，无法验证通用编码智能体在无额外定制、多智能体协作下完成跨天级复杂依赖任务的能力，而这类能力是Agent落地企业级软件、电商全链路运营等真实场景的核心要求。

### 方法关键点
- 4个同构Gemini 4 Argon通用编码智能体，无预分配角色、无游戏专属逻辑注入，仅通过标准Mineflayer开源库控制MC角色，基于游戏内聊天、团队共享记忆完成协作
- 额外配置1个独立Observer智能体全程无干预校验过程，无人类介入调整策略
- 智能体自主编写JavaScript代码执行动作，自行规划任务、编写调试工具、沉淀失败规则、协商分工、回收队友掉落物资

### 关键结果
从随机生成的Easy难度存档从零开始，27小时14分钟完成击败末影龙目标，全程编写2783个JS程序，累计63313行代码，交换229条协作消息，死亡605次；总token消耗13.5亿输入、1600万输出，91%输入token来自KV cache，按公开报价成本仅520美元；是首个无人类定制游戏工具、无预设种子的端到端自主通关MC的方案。

### 最值得记住的一句话
通用编码智能体仅靠基础通用规则和团队协作，就能完成跨天级、数千步依赖的复杂任务，离落地真实企业级场景仅一步之遥
