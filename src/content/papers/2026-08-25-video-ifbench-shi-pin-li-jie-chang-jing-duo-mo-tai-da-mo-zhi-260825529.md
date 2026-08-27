---
title: 'Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video
  Understanding Scenarios'
title_zh: Video-IFBench：视频理解场景多模态大模型指令跟随能力评估基准
authors:
- Hongbo Liu
- Peixian Chen
- Sihan Liu
- Peiyuan Zhang
- Kai Zou
- Dian Zheng
- Xiaoxing Hu
- Yuhao Dong
- Mengdan Zhang
- Yunhang Shen
affiliations:
- TJU
- Tencent Youtu Lab
- SJTU
- Tencent Hunyuan
- CUHK
arxiv_id: '2608.25529'
url: https://arxiv.org/abs/2608.25529
pdf_url: https://arxiv.org/pdf/2608.25529
published: '2026-08-25'
collected: '2026-08-27'
category: Eval
direction: 多模态大模型 · 视频理解指令跟随评测
tags:
- MLLM
- Evaluation Benchmark
- Video Understanding
- Instruction Following
- Multimodal
one_liner: 构建覆盖32类任务39种约束的视频MLLM指令跟随评估基准，实测20+主流模型暴露能力短板
practical_value: '- 短视频电商多模态Agent开发可复用该基准的4类指令模板（单/多任务/选择/嵌套）构造测试集，验证Agent对复杂用户查询的指令遵从度，降低答非所问概率

  - 短视频内容标签、商品理解标注流程可参考其半自动化构造pipeline：MLLM生成初版+程序规则校验+人工抽检，大幅降低标注成本，适合快速扩充垂类数据集

  - 优化短视频搜索推荐的query理解模块时，可参考其39种约束分类体系，对用户query的语义/格式/多条件约束做结构化拆解，提升召回排序精准度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM视频理解评测仅关注任务准确率，缺失对用户指令约束遵从度的评估，无法适配真实场景中用户多样化指令要求。
### 方法关键点
1. 搭建4类指令模板体系：覆盖单任务、多任务、选择、嵌套指令，包含32种任务类型、39种手动设计的语义/格式约束分类；
2. 搭建半自动化数据构造pipeline：结合MLLM生成、程序化处理、人工校验，大幅降低标注成本；
3. 最终构造1.5K高质量评测样本，覆盖音视频多模态内容约束。
### 关键结果
实测20+主流MLLM，当前模型视频指令跟随能力普遍较差，尤其在多约束、语义约束、需基于视频内容选分支的复杂条件结构指令上短板明显。
