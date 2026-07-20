---
title: 'MM-IssueLoc: A Controlled Benchmark for Evaluating Visual Evidence in Multimodal
  Repository-Level Issue Localization'
title_zh: MM-IssueLoc：多模态仓库级问题定位视觉证据评估可控基准
authors:
- Shaoxiong Zhan
- Shi Hu
- Boyu Feng
- Hai Lin
- Andrew Gong
- Zhengda Zhou
- Jiaying Zhou
- Yunyun Hou
- Hao Su
- Hai-Tao Zheng
affiliations:
- Tsinghua University
- JD.com
arxiv_id: '2607.15205'
url: https://arxiv.org/abs/2607.15205
pdf_url: https://arxiv.org/pdf/2607.15205
published: '2026-07-16'
collected: '2026-07-20'
category: Eval
direction: 多模态仓库问题定位评测基准构建
tags:
- Multimodal Benchmark
- Issue Localization
- LLM Evaluation
- Software Engineering
- Vision-Language
one_liner: 构建含652个标注样本的多模态仓库问题定位可控基准，解耦定位与补丁生成任务
practical_value: '- 做带多模态输入的Agent评测时，可参考其纯文本/带模态配对评测设计，精准剥离模态增益的混淆变量

  - 处理含视觉证据的用户问题定位（如电商用户反馈截图、系统报错UI）时，可复用其VCE图像转结构化文本证据的诊断方法

  - 构建跨模态召回/定位数据集时，可参考其7类图像、4级相关性的分层标注体系'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有仓库级问题定位评测多为纯文本任务，多模态软件工程基准耦合定位与补丁合成流程，无法明确视觉输入对任务的实际作用。
### 方法关键点
构建MM-IssueLoc可控基准，覆盖23种语言的652条issue-PR实例，标注7类图像、4级相关性，提供文件/函数级金标，支持纯文本/带图像配对评测，配套VCE工具将图像转换为结构化文本证据，同时给出基线多模态检索器MM-IssueLoc-VL-Emb。
### 关键结果数字
现有系统性能远未达可靠水平：最强Agent的file Acc@5为38.96%、function Acc@10为22.45%，最强检索器的function Acc@10仅33.86%；文本主导的SWE基准上的高定位得分无法直接迁移到多模态场景。
