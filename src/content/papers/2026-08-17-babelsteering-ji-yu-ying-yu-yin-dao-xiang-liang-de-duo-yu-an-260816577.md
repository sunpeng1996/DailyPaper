---
title: 'BabelSteering: Multilingual Safety Alignment via English Steering Vectors'
title_zh: BabelSteering：基于英语引导向量的多语言安全对齐方法
authors:
- Emma V. Stein
- Dominik Meier
- Terry Ruas
- Jan Philip Wahle
- Bela Gipp
affiliations:
- University of Göttingen, Germany
- German State Police NRW, Germany
arxiv_id: '2608.16577'
url: https://arxiv.org/abs/2608.16577
pdf_url: https://arxiv.org/pdf/2608.16577
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: 多语言LLM 推理时安全对齐
tags:
- Safety Alignment
- Activation Steering
- Multilingual LLM
- Inference Intervention
- Cross-lingual Transfer
one_liner: 基于英语激活引导向量实现无需多语言标注的轻量LLM多语言安全对齐
practical_value: '- 做多语言跨境电商Agent/导购LLM时，无需各语言安全标注，仅用100+条英语样本提取引导向量即可快速实现跨语言安全对齐，大幅降低标注成本

  - 可通过调整α（拒答强度）和λ（正交化系数）两个超参数快速适配业务场景：高安全要求的客服场景调大α提升拒答率，高灵活性要求的内容生成场景调小λ降低误拒

  - 多语言安全评估可复用论文的「输出翻译+WildGuard分类」pipeline，无需开发各语言的拒答关键词匹配规则，减少工程工作量

  - 引导向量可预计算后直接固化到模型权重，无推理额外开销，适配高QPS的在线推荐/广告/客服业务场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM安全对齐资源高度集中于英语，非英语用户面对相同模型时安全防护更弱；传统多语言安全对齐依赖各语言标注成本极高，全量微调还易引发多语言性能坍缩，亟需低成本、无需多语言数据的跨语言安全对齐方案。
### 方法关键点
- 仅用128条英语标注样本，分别提取有害请求真拒答向量、伪有害请求误拒向量，对两个向量做正交化处理，明确真实有害和疑似有害的表征边界
- 推理时在指定残差层加入真拒答向量提升有害请求拒答率，同时消融正交化后的误拒向量，降低对合法请求的误拒
- 向量可预计算后直接折叠进模型权重，推理时无额外计算开销，无需模型重训
### 关键实验结果
覆盖Gemma 7B、Llama 3.1 8B、Qwen 7B三个主流开源模型，测试8种高低资源语言：Gemma 7B多语言有害请求拒答率平均提升11pp，低资源语言孟加拉语提升17pp，Global MMLU通用能力无损失，伪有害请求误拒平均提升13pp；通过超参数调整可灵活平衡安全、误拒、效用三者的tradeoff。
### 核心结论
LLM的拒答方向在不同语言的隐空间中高度通用，仅用英语安全数据即可低成本覆盖绝大多数跨语言通用安全场景
