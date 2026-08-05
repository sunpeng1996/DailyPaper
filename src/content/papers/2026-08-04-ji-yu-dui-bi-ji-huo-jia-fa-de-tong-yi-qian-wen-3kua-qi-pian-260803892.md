---
title: Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition
title_zh: 基于对比激活加法的通义千问3跨期偏好调控
authors:
- Michal Mráz
- Justin Shenk
affiliations:
- Independent
arxiv_id: '2608.03892'
url: https://arxiv.org/abs/2608.03892
pdf_url: https://arxiv.org/pdf/2608.03892
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM 激活工程 · 偏好调控
tags:
- Contrastive Activation Addition
- Activation Steering
- Intertemporal Preference
- Mechanistic Interpretability
- Qwen3
one_liner: 通过对比激活加法定位通义千问3的时间偏好线性方向，可双向调控跨期选择并提升长程规划能力
practical_value: '- 导购、理财类推荐Agent场景，可通过CAA构造时间偏好方向，无需SFT即可快速调整模型给出的短期/长期消费建议倾向，适配不同用户画像

  - 长程任务（如用户年度消费规划、多步出行方案生成）Agent，可通过中等强度的长期方向steering提升规划合理性，效果比prompt调教更稳定

  - 电商分期、理财产品推荐场景中，可基于该方法测量模型内置的时间偏好阈值，校准推荐内容与用户真实风险承受能力的匹配度

  - 激活steering优先选择64层Transformer的中后24~48层，扰动幅度控制在残差norm的8%以内时，对模型生成质量的负面影响最小'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前大语言模型在输出涉及跨期权衡的建议（如消费、理财、规划类内容）时，内置时间偏好是预训练与指令微调的黑盒产物，无法根据场景需求灵活调整，易出现推荐建议与用户真实风险承受能力、长期利益 mismatch 的问题，亟需轻量、可解释的偏好调控手段。
### 方法关键点
- 基于Qwen3-32B，构造500条带明确时间标记、300条隐含时间语义的跨期选择对比数据集，每条样本对应短期/长期两个教师强制回答
- 提取模型中后段24~48层残差流激活，计算长期回答平均激活与短期回答平均激活的差值，生成归一化时间偏好调控向量d_MM
- 推理阶段在prompt最后一个token及每步解码的对应层叠加带符号、强度的d_MM：正向强度引导长期偏好，负向强度引导短期偏好
### 关键实验结果
1. 二选一跨期选择任务：d_MM作为探针在外显测试集准确率达96%，跨隐含语义集准确率达77%；±128强度调控下，外显集长期选择率差达59.4pp
2. 跨域货币跨期选择任务：10年延迟场景下，负向调控要求的延迟奖励倍数是正向调控的56倍，全延迟平均几何AEIM比值达4.9
3. TravelPlanner规划基准：中等强度正向（长期）调控可提升常识约束通过率，强度过大会导致生成 coherence 下降
### 核心结论
基于对比激活加法构造的语义方向向量可跨任务泛化，无需重新训练即可精准调控LLM的高阶偏好和能力倾向。
