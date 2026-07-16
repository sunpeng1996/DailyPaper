---
title: 'SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding'
title_zh: SynthDocBench：长上下文视觉文档理解可控基准
authors:
- Abhigya Verma
- Khyati Mahajan
- Amit Kumar Saha
- Shruthan Radhakrishna
- Sagar Davasam
- Vikas Yadav
- Sai Rajeswar Mudumba
affiliations:
- ServiceNow AI
- Mila
- Université de Montréal
arxiv_id: '2607.10400'
url: https://arxiv.org/abs/2607.10400
pdf_url: https://arxiv.org/pdf/2607.10400
published: '2026-07-10'
collected: '2026-07-16'
category: Eval
direction: 长上下文多模态文档理解评测
tags:
- VLM
- Long-Context
- Document Understanding
- Benchmark
- Multimodal Eval
one_liner: 提出可控变量的合成长上下文视觉文档理解基准，定位现有VLM三类未被发现的失效模式
practical_value: '- 搭建内部业务评测集时可参考组合式变量控制设计，独立调整文档长度、布局、问题类型等维度，精准定位模型失效原因，降低上线风险

  - 处理电商商品手册、商户资质、广告方案等多模态长文档的Agent，可参考VLM位置敏感性结论，将关键信息避开文档中间1/3区域放置，提升信息提取准确率

  - 构建合成训练/评测数据集时，可复用40%随机覆写的trick，避免模型学习到虚假关联，提升模型/评测的鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM文档理解基准无法解耦文档长度、布局复杂度、模态组成等变量，难以精准定位模型失效的具体原因，且基准的文档长度和结构多样性不足，无法匹配真实场景需求。
### 方法关键点
1. 采用组合式设计构建全合成基准SynthDocBench，独立控制文档长度、布局结构、模态组成、问题类型四类变量，支持可控的模型行为分析；
2. 基于LLM流水线生成覆盖6种布局原型的文档，加入40%随机覆写避免模型学习虚假关联；
3. 基准覆盖的长文档长度和结构多样性远超现有同类基准。
### 关键结果数字
测试7个前沿VLM，发现三类现有基准无法暴露的失效模式：模型性能随文档长度提升急剧下降；5/6的模型存在位置敏感性，文档中间1/3内容最难识别，性能从开头到结尾最高下降8.3个百分点；长文档场景下图表理解能力大幅下降，证明现有VLM多存在基准过拟合问题，鲁棒性不足。
