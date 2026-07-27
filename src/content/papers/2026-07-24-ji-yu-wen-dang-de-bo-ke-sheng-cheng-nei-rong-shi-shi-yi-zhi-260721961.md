---
title: On Improving Faithfulness of Podcasts from Documents
title_zh: 基于文档的播客生成内容事实一致性提升研究
authors:
- Soumya Dutta
- Tejas Indulal Dhamecha
- Pannaga Shivaswamy
affiliations:
- Indian Institute of Science
- Adobe Research
arxiv_id: '2607.21961'
url: https://arxiv.org/abs/2607.21961
pdf_url: https://arxiv.org/pdf/2607.21961
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: LLM 长文本生成事实一致性优化
tags:
- Faithfulness
- LLM-as-judge
- Hallucination Mitigation
- Long-form Generation
- LoRA
one_liner: 提出对话轮次级事实一致性评估方案与模型无关的catch-n-repair幻觉修正框架
practical_value: '- 轮次级检测+后修复的pipeline可直接迁移到电商生成式客服、商品文案、种草内容的幻觉修正，无需修改原生成模型，完美适配闭源黑盒LLM场景

  - turn级LLM-as-judge评估方案可替换RAG、生成式推荐系统中原有的事实性校验指标，和人类判断的相关性比传统token重叠、BERTScore类指标高40%以上

  - 用小参数LLM做LoRA微调训练幻觉检测器的思路，比直接调用大模型做judge成本降低70%以上，适合直播脚本、批量商品文案的高吞吐线上审核场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于LLM的文档转播客等长文本多轮生成系统普遍存在幻觉问题，常引入源文档未提及的信息，而现有研究多聚焦生成内容的流畅度、结构，缺乏针对长文本多轮场景的事实一致性系统研究，传统短文本事实性评估指标无法适配多轮对话的细粒度校验需求。

### 方法关键点
- 评估层：设计对话轮次（turn）级的LLM-as-judge评估协议，采用1-5分李克特量表对每个对话轮次的事实一致性打分，与人类标注的相关性远高于传统K-F1、BERTScore等指标
- 修正层：提出catch-n-repair框架，模型无关适配闭源/开源LLM：先用大模型生成忠实/非忠实对话轮次的标注数据集，再通过LoRA微调小参数LLM作为catch检测器识别非忠实轮次，最后触发原生成模型基于源文档重写该轮内容，保留对话流畅度

### 关键实验
基于1520份覆盖学术、法律、政策、金融、医疗5个领域的文档构建测试集，对比GPT-4o、LLaMA3.3-70B、Qwen2.5系列等主流生成模型，catch-n-repair在域内测试集平均提升事实性得分0.1-0.3，域外测试集平均提升0.2-0.5，同时对源文档内容覆盖率的影响小于0.2分，无明显信息损失。

### 核心结论
长文本多轮生成的事实一致性优化无需改动底座模型，轻量的轮次级检测+后修复即可实现显著提升，且跨域泛化性优异。
