---
title: Delegating or Doing? Understanding User Behavior in Hybrid Human-Agent Interfaces
title_zh: 混合人机界面下用户自主操作与委托Agent行为模式研究
authors:
- Gavin Raine Dizon
- Tyrone Justin Sta Maria
- Jordan Aiko Deja
- Yasuyuki Sumi
affiliations:
- Future University Hakodate
- De La Salle University
arxiv_id: '2608.19551'
url: https://arxiv.org/abs/2608.19551
pdf_url: https://arxiv.org/pdf/2608.19551
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: 人机交互 · 用户Agent委托行为
tags:
- Human-Agent Interaction
- Delegation Behavior
- Model Context Protocol
- Hybrid Interface
- User Behavior
one_liner: 通过73人对照实验揭示混合人机界面用户委托Agent行为规律，核心收益为降低操作复杂度而非提升速度
practical_value: '- 搭建电商商家后台、运营工具类Agent产品时，无需强制引导用户使用Agent，将入口做醒目即可，用户委托倾向由个人特质主导，强制引导收益极低

  - 优化Agent功能时优先提升单次委托的效率：包括意图识别准确率、执行结果的可视化反馈，无需投入过多资源做多轮对话交互，多数用户仅做少量高价值委托

  - Agent执行高风险操作（如商品改价、优惠券发放、内容删除）时必须加强校验、可回滚机制，不要假设用户会因操作风险高而避免委托，实验显示删除类操作委托率并不低

  - 评估Agent产品价值时不要仅用任务耗时作为核心指标，需补充点击量、页面跳转次数等操作负担类指标，这类指标才能真正体现Agent的实际价值'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM Agent已广泛嵌入各类应用，用户可选择通过传统GUI自主操作，也可委托Agent执行任务，但两种交互模式并存时用户的选择规律、不同模式的实际收益差异缺乏实证支撑，尤其是CRUD这类通用操作场景下的用户行为特征不明确，直接制约混合人机界面的设计效果。
### 方法关键点
- 基于MCP协议搭建同时支持GUI操作和Agent交互的CMS系统，无需修改原有REST API即可将现有功能暴露给Agent调用，Agent执行完成后自动跳转对应页面为用户提供可视化反馈
- 采用被试间实验设计，73名参与者分为三组：仅传统GUI组、混合模式组（两种操作均支持无引导）、AI优先组（引导尽量使用Agent），所有参与者完成16个覆盖全部CRUD类型的固定任务
- 采集指标包括任务耗时、点击/滚动/页面跳转次数、Agent交互次数
### 关键结果
- 三组任务耗时无显著差异：AI优先组平均46.6s、传统组48.2s、混合组51.9s，p=0.772
- AI辅助模式大幅降低操作负担：AI优先组相比传统组点击数下降42.8%、页面跳转数下降27.1%，均达到p<0.001的显著水平
- 用户委托行为与任务风险无显著关联，删除操作的Agent交互率反而略高于更新操作
- 个体差异解释了50%的Agent使用方差，远高于任务类型的影响
### 核心结论
混合人机界面的核心价值是降低用户操作负担而非提升任务速度，用户是否委托Agent更多由个人特质决定而非任务本身
