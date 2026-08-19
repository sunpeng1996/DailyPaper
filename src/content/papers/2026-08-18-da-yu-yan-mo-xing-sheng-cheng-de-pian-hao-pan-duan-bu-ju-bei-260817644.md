---
title: LLM-Derived Preference Judgments Are Not Self-Consistent
title_zh: 大语言模型生成的偏好判断不具备自洽性
authors:
- Matthew T. Ford
- Francis Bahk
- Jingjing Wang
- Adam S. Jovine
- Tinghan Ye
- David B. Shmoys
- Peter I. Frazier
affiliations:
- Cornell University
- Georgia Institute of Technology
arxiv_id: '2608.17644'
url: https://arxiv.org/abs/2608.17644
pdf_url: https://arxiv.org/pdf/2608.17644
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM偏好判断 · 自洽性审计
tags:
- Preference Judgment
- Utility Function
- Self-Consistency
- LLM Evaluation
- Prompt Elicitation
one_liner: 提出偏好自洽性审计框架，验证6款LLM的数值偏好无法被单一效用函数拟合
practical_value: '- 用LLM做用户偏好 elicitation（如个性化推荐、生活服务Agent需求理解）时，不能默认不同提问方式的结果可互换，需先在业务场景做自洽性校验，优先选择偏好输出稳定的LLM

  - 涉及商品定价、用户支付意愿估算的场景，不要混用「单商品最高出价」和「双商品差价补偿」两类提问结果，否则会出现2.1%~12.5%的偏好反转，导致推荐结果偏离用户预期

  - 可复用论文的自洽性审计框架（P1/P2局部校验、全局RMSE拟合度检验），上线前验证自有Prompt、LLM在业务场景下的偏好判断稳定性，减少框架效应带来的误差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前越来越多Agent、推荐系统依赖LLM将用户自然语言偏好转换为结构化数值判断（如支付意愿、偏好得分），再拟合效用函数做决策，但其默认前提是LLM的偏好判断自洽、可被单一效用函数拟合，该假设从未被系统性验证，一旦不成立会直接导致下游决策偏离用户需求。

### 方法关键点
- 设计两类标准化提问：①Item query：直接询问用户对单商品的最高支付意愿；②Offer-pair query：询问两个带价商品的差价调整多少时用户会保持中立
- 定义自洽性假设HSC：两类提问的结果均值可被同一个准线性货币效用函数拟合，配套两类校验规则：P1校验直接询问的双商品差价与分步询问的路径求和差价是否一致，P2校验双商品差价与两个单商品支付意愿的调整差值是否一致，搭配全局bootstrap检验拟合RMSE的显著性
- 实验覆盖3个高 stakes 决策领域（机票、租房、酒店）、3种不同偏好侧重的用户话术、6款主流LLM，每个提问重复15次控制抽样误差

### 关键结果
所有6款LLM全部拒绝自洽性假设，其中5款在全部9个测试组上显著不通过；全局拟合RMSE在机票/租房场景占商品均价的1.6%~6.1%，酒店场景达18.9%~44.9%；P2校验的不通过率达41.7%~87.5%，2.1%~12.5%的案例出现完全偏好反转，不同提问方式得到的结果会选出完全相反的商品。

最值得记住的一句话：LLM的偏好判断结果高度依赖提问方式，未做业务场景一致性校验时，不要直接假设其可被单一效用函数拟合用于下游决策。
