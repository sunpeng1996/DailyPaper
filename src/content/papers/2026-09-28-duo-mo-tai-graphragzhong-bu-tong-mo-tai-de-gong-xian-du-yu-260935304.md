---
title: Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG
title_zh: 多模态GraphRAG中不同模态的贡献度与协同效应分析
authors:
- Antonios Georgakopoulos
- Paul Groth
- Lise Stork
affiliations:
- University of Amsterdam
arxiv_id: '2609.35304'
url: https://arxiv.org/abs/2609.35304
pdf_url: https://arxiv.org/pdf/2609.35304
published: '2026-09-28'
collected: '2026-09-29'
category: RAG
direction: 多模态GraphRAG 模态贡献分析与检索优化
tags:
- Multimodal-GraphRAG
- Modality-Contribution
- Shapley-Value
- DocVQA
- Modality-Aware-Retrieval
one_liner: 基于Shapley值量化多模态GraphRAG模态贡献与协同，验证选择性检索的价值
practical_value: '- 电商/广告多模态RAG构建时，为每个检索chunk/知识图谱三元组打上来源模态标签，默认优先检索Text和Table模态，可直接过滤贡献极低的Layout模态，降低检索与推理成本

  - 用SHAPE类Shapley值方法量化不同模态对业务场景的实际贡献，不要盲目堆多模态：小参数MLLM部署场景可直接忽略Image模态，仅保留Text+Table即可达到90%以上的全模态效果

  - 针对query类型动态选模态：计算类/定位类query（如查商品价格、尺寸、优惠组合）补充Image+Table模态可获协同增益，普通属性查询类query只用Text即可，避免冗余拉低准确率

  - 全模态检索时需过滤Text与其他模态的重复内容，避免文本与其他模态的冗余信息干扰LLM推理，提升生成答案的准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态GraphRAG普遍默认引入更多模态能提升下游任务效果，但冗余/重叠的多模态证据会干扰LLM推理，不同模态的实际贡献、模态间是协同还是冗余，以及随query类型、模型能力的变化规律缺乏系统量化，无法指导高效检索策略设计。
### 方法关键点
- 改造SOTA多模态GraphRAG框架RAG-Anything，为知识图谱每个三元组标注来源模态（Text/Table/Image/Layout），支持按模态子集过滤检索结果
- 采用SHAPE（基于Shapley值）指标，量化单模态贡献度S，以及模态对的协同系数C：C>0为互补增益，C<0为冗余干扰
- 控制变量覆盖5款多模态LLM（GPT-4o-mini、Qwen3-VL 8B/30B、Gemma3 4B/27B），基于2个DocVQA benchmark中1051个标注了所需模态的双模态query做测试
### 关键结果
- 单模态贡献度排序：Table>Text>>Image>Layout，Layout贡献几乎可忽略
- 模态协同：所有包含Text的模态对协同系数均为负（存在显著冗余），仅Image+Table对在Quantity、Locating类query下有正协同
- 小参数模型（<10B）对Image模态的利用率不足大模型的30%，Image贡献极低

**最值得记住的结论**：多模态GraphRAG不应默认全模态检索，需根据query类型、部署模型能力动态选择模态子集，优先保留Text和Table可实现最优投入产出比
