---
title: Who are you? The Personal Imitation Game
title_zh: 个人模仿游戏：面向特定个体对话复刻的LLM评测框架
authors:
- Muhammad Rizky Wellyanto
- Hajara-Yasmin Isa
- Kexin Xue
- Vishal Ravichandran
- Wenpeng Lu
- Jerry O. Talton
- Ranjitha Kumar
affiliations:
- University of Illinois at Urbana-Champaign
arxiv_id: '2611.24888'
url: https://arxiv.org/abs/2611.24888
pdf_url: https://arxiv.org/pdf/2611.24888
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: 个人AI Agent · 身份复刻评测框架
tags:
- Personal Agent
- Turing Test
- RAG
- LLM Evaluation
- Persona Simulation
one_liner: 提出三角色个人模仿游戏评测框架，验证基于长期个人数据的LLM可逼真复刻特定个体对话身份
practical_value: '- 构建用户数字孪生/个人助手时，可复用「风格特征+人格特质+生平事实」三维特征框架，避免仅依赖行为数据的信息遗漏

  - 个人对话类Agent可采用「静态人格/风格prompt + 历史对话RAG」架构，无需全量微调即可获得不错的仿人效果，落地成本低

  - 账号安全/反诈骗场景可参考提取的三类身份信号（计量语言学特征、大五人格特征、生平事实）构建风控模型，提升仿冒账号识别准确率

  - 电商客服/导购Agent可复用随机延迟+固定打字速度的交互仿真策略，拉近与用户的心理距离，提升信任度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM已能通过通用图灵测试，但能否复刻特定个体的对话身份仍缺乏标准化评测框架；同时个人AI Agent、数字孪生等场景亟需可落地的个体身份建模方案，相关隐私风险也需要明确的评估范式。

### 方法关键点
- 提出三角色「个人模仿游戏」框架：审问者同时与目标、模仿者聊天，需识别真实目标，要求所有参与者互相熟悉，避免通用图灵测试的泛化问题
- 基于人类基线实验总结三类身份识别信号：计量语言学特征（词汇、语法、回复延迟等）、大五人格特质、生平事实（人口属性、经历、偏好等）
- 构建LLM模仿系统：采用RAG架构，输入目标10年跨平台聊天数据+大五人格自评+风格自评+自传，加入随机延迟、打字速度模拟人类交互行为

### 关键结果
- 人类基线：30名参与者的10组实验中，审问者识别准确率为56.7%，与随机水平无显著差异
- LLM系统评测：20名目标熟人参与测试，70%的回合审问者将LLM误认为是比人类朋友更真实的目标，35%的回合LLM成功骗过审问者伪装成目标本人，两类结果均与随机水平无显著差异
- 仅30%的参与者事后怀疑对话中有AI，未有人通过延迟特征识别出AI

**最值得记住的一句话**：定制个人Agent的核心差异点是「复现人的身份特征」而非仅「执行用户指令」，现有技术已能做到让熟人无法区分AI与真人的对话。
