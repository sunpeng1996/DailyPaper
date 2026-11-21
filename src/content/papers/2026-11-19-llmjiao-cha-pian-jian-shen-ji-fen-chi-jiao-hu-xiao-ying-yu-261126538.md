---
title: 'LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits'
title_zh: 《LLM交叉偏见审计：分离交互效应与叠加效应的新方法》
authors:
- George Rahul
- Ronit Jahilal
- Bhaskara Hanuma Vedula
- Ponnurangam Kumaraguru
- Pushkar Shukla
affiliations:
- International Institute of Information Technology Hyderabad, India
- Cloudphysician.ai, USA
arxiv_id: '2611.26538'
url: https://arxiv.org/abs/2611.26538
pdf_url: https://arxiv.org/pdf/2611.26538
published: '2026-11-19'
collected: '2026-11-21'
category: Eval
direction: LLM公平性评估 · 交叉偏见检测
tags:
- LLM Fairness
- Intersectional Bias
- Bias Audit
- Additive Model
- Hypothesis Testing
one_liner: 提出ADDIS审计框架，降低LLM交叉身份偏见检测误报，提升真实交互效应召回
practical_value: '- 电商推荐/Agent用户服务场景中，可复用ADDIS框架区分单属性偏好叠加和真实交叉群体需求，避免对小众用户群体的需求误判

  - 评估LLM生成内容（如商品文案、客服回复）的公平性时，用ARD+Freedman-Lane检验替代传统阈值规则，可大幅降低误报

  - 构建用户测试集时，可参考IndiPersona的多属性人设构造方法，覆盖更多交叉群体的边界case，提升评估完备性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM交叉身份偏见审计无统一基线，传统判定规则会将独立属性的叠加效应误判为交叉偏见，误报率极高，真实交叉效应召回率仅32%。
### 方法关键点
提出ADDIS审计框架：先拟合全属性加法模型，计算每个子群体的Additive Residual Distance(ARD)，再通过Freedman-Lane零假设检验判定是否存在真实交互效应；同时构建包含10000个6维度身份属性的印度人设测试集IndiPersona。
### 关键结果
- 合成基准测试：ADDIS单数据集平均误报子群体数从66.1降至0.09，真实交叉效应召回率从32%提升至84%
- 13个开源LLM实测：交叉子群体偏见误报率从7.1%降至3.0%，还检测到传统方法漏检的种姓×阶层交叉偏见
