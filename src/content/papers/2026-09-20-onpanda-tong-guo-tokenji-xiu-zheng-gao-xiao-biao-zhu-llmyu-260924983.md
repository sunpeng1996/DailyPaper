---
title: 'onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents
  via Token-Level Correction'
title_zh: onPanda：通过Token级修正高效标注LLM与Agent的在线对齐数据
authors:
- Lei Yang
- Mengyin Liu
- Jia Wang
- Hangyu Guo
- Liang Zhao
- Zheng Ge
- Kang An
- Binxing Jiao
- Qi Han
- Daxin Jiang
affiliations:
- StepFun
- Xiamen University
arxiv_id: '2609.24983'
url: https://arxiv.org/abs/2609.24983
pdf_url: https://arxiv.org/pdf/2609.24983
published: '2026-09-20'
collected: '2026-09-22'
category: LLM
direction: LLM与Agent对齐 · 数据标注工具
tags:
- LLM-Alignment
- Data-Annotation
- On-Policy
- Token-Level-Correction
- Agent-Trajectory
one_liner: 提出Token级修正的标注范式，较传统人工后编辑降52%标注时间，同时保留高On-Policy保真度
practical_value: '- 做生成式推荐、电商商品文案/导购话术SFT数据标注时，可复用token级修正范式，比传统人工后编辑降50%左右标注时间，同时避免人工改写带来的分布偏移，保证数据On-Policy特性

  - 落地电商导购Agent、客服Agent时，可直接复用其结构化工具调用修正能力标注Agent轨迹，自动生成的细粒度token级正负样本对可直接用于RM、DPO、PRM训练

  - 可将token概率着色的trick集成到自有生成内容审核流程，快速定位低置信度错误token，降低人工审核成本，也可用于生成式模型的bad case诊断

  - 该工具开源可直接复用，轻量部署无需数据库，支持对接自定义推理API，可快速适配电商、广告领域的特定标注需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM与Agent对齐的核心瓶颈是高质量标注数据供给，传统方案难以平衡三个核心诉求：人工撰写/后编辑标注成本高且产出数据为Off-Policy，偏好标注仅提供粗粒度响应级监督，Agent轨迹标注更缺乏支持实时工具调用修正的交互工具，无法兼顾标注效率、On-Policy保真度与监督粒度。
### 方法关键点
- 核心交互为「定位-修正-继续」的token级修正循环：标注者找到响应中第一个错误token，可从模型Top-k候选中选替代或自由编辑，系统截断后续内容从修正后前缀继续生成，直到符合质量要求
- 自动构建标注树保留所有中间版本，天然产出token级配对正负样本，可一键导出为SFT、偏好、PRM三类训练数据
- 支持结构化响应模板，兼容推理链、工具调用等Agent轨迹标注，可对接外部MCP工具与真实环境，同时支持多模态数据标注
- 可视化每个token的生成概率，低置信度token高亮提示，辅助标注者快速定位错误，也可独立用于模型行为诊断
### 关键实验
对比POTATO人工后编辑、Argilla四候选偏好排序两个主流基线，3名标注者标注21个图文描述prompt：
- 中位数标注时间330s，较POTATO的681s降低51.5%，与Argilla的336s相当；平均标注时间较两个基线分别低27.5%、24.7%
- 标注数据PPL仅比原生采样基线高0.86%，远低于POTATO的36.31%，On-Policy保真度接近模型原生分布
- SFT覆盖率100%，高于Argilla的52%；单prompt平均产出7.43个绑定修正位置的偏好对，优于两个基线
- 生产部署数据显示，合格响应中97%的token为模型生成，仅0.9%为人工输入，干预极稀疏
### 核心结论
Token级修正标注范式以极低的人工干预成本，同时实现了标注效率提升、高On-Policy保真度和细粒度监督信号的三重收益。
