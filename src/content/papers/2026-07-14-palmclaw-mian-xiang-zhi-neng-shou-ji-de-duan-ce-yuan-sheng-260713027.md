---
title: 'PalmClaw: A Native On-Device Agent Framework for Mobile Phones'
title_zh: PalmClaw：面向智能手机的端侧原生Agent运行框架
authors:
- Hongru Cai
- Yongqi Li
- Ran Wei
- Wenjie Li
arxiv_id: '2607.13027'
url: https://arxiv.org/abs/2607.13027
pdf_url: https://arxiv.org/pdf/2607.13027
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: 端侧Agent · 移动端原生框架设计
tags:
- On-Device Agent
- Mobile LLM
- Tool Calling
- Agent Framework
- Edge AI
one_liner: 提出端侧原生手机Agent框架PalmClaw，封装设备能力为标准化工具，大幅提升任务效率与成功率
practical_value: '- 可复用端侧原生工具封装思路，将电商APP内的商品搜索、加购、订单查询等能力封装为结构化调用工具，替代原有GUI交互模拟的智能导购链路，大幅降低响应耗时。

  - 端侧全链路Agent运行的架构设计，可迁移到需要处理用户隐私数据的个性化推荐场景，避免用户行为、偏好数据上传云端的合规风险。

  - 工具执行边界明确定义的设计方法，可直接应用到业务Agent的工具链开发中，减少任务执行溢出、不可控的问题。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有移动端Agent普遍依赖模拟点击、滑动、输入等GUI操作完成任务，执行链路长、强依赖界面布局、无法直接调用设备原生能力，且执行边界模糊不可控；同时移动端拥有海量用户本地数据、传感器、高频使用APP，是Agent落地的高价值场景，缺乏原生端侧框架支撑。
### 方法关键点
1. 开源端侧原生Agent框架PalmClaw，所有会话管理、内存存储、技能调度、工具调用、Agent推理循环完全在端侧运行，无需依赖云端算力；
2. 将设备传感器、APP能力等封装为具备明确入参、结构化返回值、清晰执行边界的原生工具，Agent可直接调用，无需模拟GUI操作。
### 关键结果
对比当前最强基线，任务成功率相对提升11.5%，任务完成时间降低94.9%，部署门槛更低，执行边界可控性更强。
