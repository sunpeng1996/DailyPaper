---
title: 'AutoPILOT: A Visual Agent Harness for Real-Time Gameplay'
title_zh: AutoPILOT：面向实时游戏场景的视觉Agent执行框架
authors:
- Mark Zhao
- Pengcheng Wang
- Rui Yang
- Jiarui Yao
- Xirui Jiang
- Yuxi Chen
- Bingxuan Li
- Hanyang Chen
- Ke Yang
- Manling Li
affiliations:
- University of Illinois Urbana-Champaign
- Georgia Institute of Technology
- Northwestern University
arxiv_id: '2611.28202'
url: https://arxiv.org/abs/2611.28202
pdf_url: https://arxiv.org/pdf/2611.28202
published: '2026-11-19'
collected: '2026-11-24'
category: Agent
direction: 视觉Agent · 实时交互执行优化
tags:
- Agent
- Real-time Interaction
- Visual Agent
- Harness Design
- LLM Agent
one_liner: 支持单次LLM调用输出宏/闭环控制器，大幅提升实时交互Agent成功率并降低调用成本
practical_value: '- 实时交互类Agent（如电商直播场控、智能客服、推荐系统实时干预）可复用「慢LLM决策+快代码执行」分层架构：仅在场景切换或异常时调用大模型生成执行逻辑，日常交互跑预生成的控制器/宏，降低延迟90%以上同时大幅削减LLM调用成本

  - 生成式推荐、动态文案生成等场景可参考宏执行设计：将用户进店后的多步动作序列（弹窗、推荐位排序、优惠券推送逻辑）预生成为宏，无需每步请求LLM，在保障个性化的同时将响应延迟压缩到百毫秒级

  - Agent工程实现可直接复用三类执行模式+唤醒事件的设计：根据业务对延迟的敏感度，灵活选择单步/宏/控制器执行逻辑，通过场景突变、超时等唤醒事件自动切回大模型决策，平衡效果、实时性与成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉Agent框架默认遵循「单次模型调用→输出单步动作」的执行逻辑，假设环境会暂停等待模型推理，在游戏、实时GUI交互等环境持续运行的场景中，LLM数秒级的推理延迟会导致动作过时、执行效率极低，仅优化模型的输入感知、记忆模块无法解决该瓶颈。
### 方法关键点
- 三类执行模式：单次LLM调用可选择三类输出：单步原生动作、开环固定动作序列宏、带环境感知能力的闭环Python控制器，后两类无需后续LLM调用即可自主执行多步动作，控制器可按约0.4s的间隔自主感知环境输出动作
- 唤醒机制：设计6种触发事件（控制器主动切回、宏执行完成、决策页面出现、场景突变、超时、执行报错），自动将控制权交还给大模型重新决策，保障执行安全
- AFK-Bench基准：构建包含120个浏览器游戏的评测集，按无动作惩罚程度分为敌对实时、良性实时、回合制三类，支持实时/暂停两种时钟模式，可量化评估Agent的实时性能损耗
### 关键结果
- 基于GPT-6.1 Sol对比SOTA框架VISTA：AFK-Bench全实时场景成功率68.6% vs 38.3%，敌对实时场景下62.5% vs 16.7%，GameWorld基准实时场景下80.0% vs 42.9%
- 资源消耗降低47%，达到VISTA相同成功率仅需20%的API成本，性能提升在6款不同LLM上均一致
### 核心结论
Agent框架设计中，模型输出到动作的时序执行逻辑，和模型的感知、记忆模块同等重要
